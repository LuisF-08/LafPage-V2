<template>
  <div class="flex flex-col items-center gap-6 w-full text-white p-4">
    <h2 class="text-2xl font-bold">Busca de Boletos</h2>

    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 w-full max-w-5xl bg-gray-800 p-4 rounded-lg">

      <div class="flex flex-col">
        <label class="text-sm text-gray-400">ID do Boleto</label>
        <input v-model="filtroId" type="text" placeholder="Ex: 12"
            class="bg-gray-700 p-2 rounded border border-gray-600
             focus:outline-none focus:border-blue-500 text-white" />
      </div>

      <div class="flex flex-col">
        <label class="text-sm text-gray-400">Data de Emissão</label>
        <input v-model="filtroData" type="date"
            class="bg-gray-700 p-2 rounded border
             border-gray-600 focus:outline-none focus:border-blue-500 text-white" />
      </div>

      <div class="flex items-end">
        <button type="button" @click="carregarBoletos"
                class="w-full bg-blue-600 hover:bg-blue-500 py-2 rounded font-bold transition-colors">
          Filtrar
        </button>
      </div>
    </div>

    <div class="overflow-x-auto w-full max-w-5xl bg-gray-900 rounded-lg p-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-gray-700 text-gray-300">
            <th class="p-3">ID</th>
            <th class="p-3">Código de Barras</th>
            <th class="p-3">Emitido</th>
            <th class="p-3">vencimento</th>
            <th class="p-3">Parcelas</th>
            <th class="p-3">Valor</th>
            <th class="p-3 text-center">Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="boleto in boletosVisiveis" :key="boleto.id"
              class="border-b border-gray-800 hover:bg-gray-800">
            <td class="p-3">{{ boleto.id }}</td>
            <td class="p-3 flex items-center gap-2">
            <span class="truncate max-w-[200px]" :title="boleto.codigo_de_barras">
              {{ boleto.codigo_de_barras }}
            </span>
            <button @click="copiar(boleto.codigo_de_barras)"
            class="flex-shrink-0 transition-colors"
            :class="copiado === boleto.codigo_de_barras ? 'text-green-400' : 'text-gray-400 hover:text-white'"
            title="Copiar código">
              <svg v-if="copiado === boleto.codigo_de_barras"
            xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none"
            viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none"
            viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2
            m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
              </svg>
            </button>
            </td>
            <td class="p-3">{{ formatarData(boleto.criado_em) }}</td>
            <td class="p-3">{{ formatarData(boleto.vencimento) }}</td>
            <td class="p-3">{{ boleto.parcelas || '---' }}X</td>
            <td class="p-3">R$ {{ boleto.valor_total || '---' }}</td>
            <td class="p-3 text-center">
              <button @click="fazerDownload(boleto.id)"
                      class="bg-blue-600 hover:bg-blue-500 px-4 py-1 
                      rounded-md text-sm">
                Baixar PDF
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <div v-if="boletos.length === 0" class="text-center py-10 text-gray-500">
        Nenhum boleto encontrado com esses filtros.
      </div>

      <div v-if="temMais" class="flex justify-center mt-4">
        <button @click="verMais"
                class="bg-gray-700 hover:bg-gray-600 px-6 py-2 rounded font-semibold transition-colors text-sm">
          Ver mais ({{ boletos.length - limite }} restantes)
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { buscar_boletos, baixar_pdf_boleto } from '../services/api';

const props = defineProps({
  cnpj: { type: String, required: true }
});

const boletos = ref([]);
const filtroId = ref('');       
const filtroData = ref('');      
const limite = ref(5);
const copiado = ref(null);

const boletosVisiveis = computed(() => boletos.value.slice(0, limite.value));
const temMais = computed(() => boletos.value.length > limite.value);

const verMais = () => { limite.value += 5; };

const formatarData = (dataStr) => {
  if (!dataStr) return '---';
  return new Date(dataStr).toLocaleDateString('pt-BR');
};

const carregarBoletos = async () => {
  if (!props.cnpj) return;
  const cnpjLimpo = props.cnpj.replace(/\D/g, '');
  limite.value = 5;

  const filtros = Object.fromEntries(
    Object.entries({
      id: filtroId.value,
      criado_em: filtroData.value,}).filter(([_, v]) => v !== '' && v != null)
  );

  try {
    const dados = await buscar_boletos(cnpjLimpo, filtros);
    boletos.value = Array.isArray(dados) ? dados : [];
  } catch (error) {
    console.error("Erro ao buscar boletos:", error);
    boletos.value = [];
  }
};

const fazerDownload = async (id) => {
  try {
    const blob = await baixar_pdf_boleto(id);
    const url = window.URL.createObjectURL(new Blob([blob]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `boleto_${id}.pdf`);
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error("Erro ao baixar o boleto:", error);
    alert("Não foi possível gerar o PDF agora.");
  }
};

const copiar = async (codigo) => {
  try{
    await navigator.clipboard.writeText(codigo);
    copiado.value = codigo;
    setTimeout(() => { copiado.value = null;}, 2000);
  }catch (error){
    console.error("Erro ao copiar para a área de transferência:", error);
    alert("Não foi possível copiar o código.");
  }
}

onMounted(() => carregarBoletos());
</script>