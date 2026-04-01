<template>
  <div class="flex flex-col items-center gap-6 w-full text-white p-4">
    <h2 class="text-2xl font-bold">Busca de Notas</h2>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 w-full max-w-4xl bg-gray-800 p-4 rounded-lg">
      <div class="flex flex-col">
        <label class="text-sm text-gray-400">Nº da Nota</label>
        <input v-model="filtroNfe" type="text" placeholder="Ex: 584178"
              class="bg-gray-700 p-2 rounded border border-gray-600 focus:outline-none focus:border-blue-500 text-white" />
      </div>

      <div class="flex flex-col">
        <label class="text-sm text-gray-400">Nº do Pedido</label>
        <input v-model="filtroPedido" type="text" placeholder="Ex: 4000"
              class="bg-gray-700 p-2 rounded border border-gray-600 focus:outline-none focus:border-blue-500 text-white" />
      </div>

      <div class="flex items-end">
        <button type="button" @click="carregarNotas"
                class="w-full bg-blue-600 hover:bg-blue-500 py-2 rounded font-bold transition-colors">
          Filtrar
        </button>
      </div>
    </div>

    <div class="overflow-x-auto w-full max-w-4xl bg-gray-900 rounded-lg p-4">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="border-b border-gray-700 text-gray-300">
            <th class="p-3">Nº Nota</th>
            <th class="p-3">Pedido</th>
            <th class="p-3">Data de Emissão</th>
            <th class="p-3">Valor</th>
            <th class="p-3 text-center">Ações</th>
          </tr>
        </thead>
        <tbody>

          <tr v-for="nota in notasVisiveis" :key="nota.id"
              class="border-b border-gray-800 hover:bg-gray-800">
            <td class="p-3">{{ nota.nfe }}</td>
            <td class="p-3">{{ nota.numero_pedido || '---' }}</td>
            <td class="p-3">{{  new Date(nota.criado_em).toLocaleDateString('pt-BR')|| '---' }}</td>
            <td class="p-3">R$ {{ nota.valor }}</td>
            <td class="p-3 text-center">
              <button @click="baixarXML(nota.cnpj)"
                      class="bg-blue-600 hover:bg-blue-500 px-4 py-1 rounded-md text-sm">
                Baixar XML
              </button>
            </td>
          </tr>
        </tbody>
      </table>

      <div v-if="nfea.length === 0" class="text-center py-10 text-gray-500">
        Nenhuma nota encontrada com esses filtros.
      </div>

      <div v-if="temMais" class="flex justify-center mt-4">
        <button @click="verMais"
                class="bg-gray-700 hover:bg-gray-600 px-6 py-2 rounded font-semibold transition-colors text-sm">
          Ver mais ({{ nfea.length - limite }} restantes)
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { buscar_notas_e_numeros, baixar_XML_nota_fiscal } from '../services/api';

const props = defineProps({
  cnpj: { type: String, required: true }
});

const nfea = ref([]);
const filtroNfe = ref('');
const filtroPedido = ref('');
const limite = ref(5);

const notasVisiveis = computed(() => nfea.value.slice(0, limite.value));

const temMais = computed(() => nfea.value.length > limite.value);

const verMais = () => {
  limite.value += 5; 
};

const carregarNotas = async () => {
  if (!props.cnpj) return;
  const cnpjLimpo = props.cnpj.replace(/\D/g, '');
  limite.value = 5; 

  const filtros = Object.fromEntries(
    Object.entries({
      nfe: filtroNfe.value,
      numero_pedido: filtroPedido.value
    }).filter(([_, v]) => v !== '' && v != null)
  );

  try {
    const dados = await buscar_notas_e_numeros(cnpjLimpo, filtros);
    nfea.value = Array.isArray(dados) ? dados : [];
  } catch (error) {
    console.error("Erro ao buscar dados da API:", error);
    nfea.value = [];
  }
};

const baixarXML = async (cnpjDaNota) => {
  const cnpjLimpo = String(cnpjDaNota).replace(/\D/g, '');
  try {
    const response = await baixar_XML_nota_fiscal(cnpjLimpo);
    if (!response?.data) throw new Error("Resposta da API vazia");
    const blob = new Blob([response.data], { type: 'application/xml' });
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `Nota_${cnpjLimpo}.xml`);
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error("Erro no download:", error);
    alert("Erro ao baixar o arquivo.");
  }
};

onMounted(() => carregarNotas());
</script>