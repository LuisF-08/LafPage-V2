<template>
  <div class="w-full flex flex-col min-h-screen">
    <div class="h-15 md:h-22"></div>

    <div class="w-full flex flex-col items-center pt-10 px-6 mb-16">
      <div class="relative mb-12 group">
        <div class="absolute -inset-1 blur opacity-25 rounded-3xl
         group-hover:opacity-50 transition duration-1000"></div>
        <h1 class="relative flex items-center justify-center gap-4 md:gap-6 text-center text-5xl md:text-8xl 
          bg-gradient-to-r from-blue-500 to-cyan-300 bg-clip-text text-transparent
          font-black tracking-tighter py-6 px-10 backdrop-blur-xl borderrounded-3xl">
          <i class="fa-solid fa-headset text-4xl md:text-7xl"></i>
          SAC
        </h1>
      </div>
      <div class="h-10 md:h-12"></div>

      <!-- Indicador de Etapas -->
      <div class="flex items-center gap-3 md:gap-6">
        <div v-for="i in 4" :key="i" 
          class="h-12 w-12 md:w-24 rounded-full transition-all duration-500"
          :class="etapa >= i ? 'bg-blue-500 shadow-[0_0_15px_rgba(59,130,246,0.5)]' : 'bg-white/10'">
        </div>
      </div>
    </div>
    <div class="h-5 md:h-7"></div>

    <!-- Card Principal -->
    <section class="w-full flex-1 flex items-start justify-center pb-24 px-4">
      <div class="w-full max-w-[900px] bg-slate-900/40 backdrop-blur-3xl
        border border-white/10 rounded-[2.5rem]
        shadow-2xl p-6 md:p-16 relative overflow-hidden">

        <form class="w-full" @submit.prevent="enviarFormularioSAC">
          
          <!-- ETAPA 1: Identificação -->
          <div v-if="etapa === 1" class="flex flex-col items-center gap-10 w-full">
            <h2 class=" text-white text-3xl font-bold tracking-tight">Identificação CNPJ</h2>
            <p class="text-blue-200 text-sm text-center italic leading-relaxed bg-white/5 rounded-2xl border border-white/5">
                <span class="text-[20px] text-blue-500 font-black uppercase block opacity-50 tracking-widest">
                  <strong>DICA:</strong>
                </span>
                "Se estiver com pressa e não quiser preencher o formulário,
                basta clicar em no botão de Whattsapp para niciar o atendimento"
              </p>
            <div class="flex flex-col w-full max-w-md gap-4">
              <input v-model="cnpj" @input="formatarCnpj" maxlength="18"
                placeholder="00.000.000/0000-00"
                class="w-full p-5 rounded-2xl bg-white/5 border border-white/10 text-white text-center text-2xl outline-none focus:ring-2 focus:ring-blue-500/50 transition-all font-mono">
              <button @click="validarCNPJDaEmpresa" type="button" 
                :disabled="cnpj.length < 18" 
                class="w-full py-5 bg-blue-600 hover:bg-blue-500 active:scale-[0.97] disabled:opacity-30 text-white rounded-2xl font-bold text-lg transition-all shadow-lg shadow-blue-500/20">
                Continuar
              </button>
            </div>
          </div>

          <!-- ETAPA 2: Assunto -->
          <div v-if="etapa === 2" class="flex flex-col gap-8">
            <p class="text-blue-400 text-xs text-center tracking-[0.3em] uppercase font-black">Selecione o Assunto</p>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <button v-for="(dados, label) in assuntos" :key="label"
                @click="form.assunto = label" type="button"
                :class="[
                  'flex flex-col items-center p-6 rounded-2xl border transition-all duration-200 active:scale-95',
                  form.assunto === label ? 'border-blue-500 bg-blue-500/10 ring-2 ring-blue-500/20' : 'border-white/5 bg-white/5 hover:bg-white/10'
                ]">
                <img :src="dados.imagem" class="h-14 w-14 object-contain mb-4" :alt="label">
                <span class="text-white text-sm font-bold">{{ label }}</span>
              </button>
            </div>
          
            <!-- campo selecão de suporte -->
            <div class="min-h-[110px] flex items-center justify-center bg-white/5 rounded-2xl border border-white/5 p-5">
              <p v-if="form.assunto" class="text-blue-200 text-sm text-center italic leading-relaxed">
                <span class="text-[10px] font-black uppercase block mb-1 opacity-50 tracking-widest">Informação</span>
                "{{ assuntos[form.assunto].descricao }}"
              </p>
              <p v-else class="text-slate-500 text-sm italic">Selecione um dos assuntos acima para prosseguir.</p>
            </div>

            <!-- Botões -->
            <div class="flex flex-col-reverse sm:flex-row gap-4">
              <button @click="etapa = 1" type="button" 
                class="w-full sm:w-1/3 py-4 text-slate-400 font-bold hover:text-white transition-colors">
                Voltar
              </button>
              <button @click="mostrarModal = true" :disabled="!form.assunto" type="button" 
                class="w-full sm:w-2/3 py-4 bg-blue-600 text-white rounded-xl font-bold active:scale-[0.97] transition-all disabled:opacity-20 shadow-xl shadow-blue-500/10">
                Próximo Passo
              </button>
            </div>
          </div>

        <div v-if="etapa === 3" class="flex flex-col gap-8 animate-fade-in">
          <h2 class="text-white text-3xl font-bold text-center mb-2">
            Itens da Nota Fiscal
          </h2>
          <div class="overflow-x-auto rounded-xl border border-white/10">
            <table class="w-full text-sm text-left text-gray-300">
              <thead class="whitespace-nowrap bg-white/10 text-gray-300 uppercase text-xs font-semibold">
                <tr>
                  <th class="p-4">Selecionar</th>
                  <th class="p-4">ID</th>
                  <th class="p-4">Produto</th>
                  <th class="p-4">Quantidade</th>
                  <th class="p-4">Valor</th>
                  <th class="p-4">Codigo</th>
                  <th class="p-4">Data</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in itensNota" :key="item.id" class="border-t border-white/10 hover:bg-white/5 transition-colors">
                  <td class="p-4 text-center whitespace-nowrap">
                    <input type="checkbox" v-model="itensSelecionados" :value="item" class="w-4 h-4 accent-blue-500">
                  </td>
                  <td class="p-4 whitespace-nowrap">{{ item.id }}</td>
                  <td class="p-4 whitespace-nowrap font-medium text-white">{{ item.nome_produto }}</td>
                  <td class="p-4">
                    <input 
                      type="number"
                      min="1"
                      :max="item.quantidade"
                      v-model.number="item.quantidadeDevolucao"
                      class="w-24 p-2.5 rounded-lg bg-slate-800/50 border
                      border-white/20 text-white outline-none
                      focus:border-blue-500 transition-all">
                  </td>
                  <td class="p-4 whitespace-nowrap">R$ {{ item.valor_total }}</td>
                  <td class="p-4 whitespace-nowrap">{{ item.codigo_produto }}</td>
                  <td class="p-4 whitespace-nowrap">{{ new Date(item.solicitado).toLocaleDateString('pt-BR') }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="flex flex-col-reverse sm:flex-row gap-4 mt-4 w-full">

  <button @click="etapa = 2" type="button"
    class="w-full sm:w-1/3 py-4 
    text-gray-400 hover:text-white hover:bg-white/5 
    rounded-xl transition-all font-medium">
    Voltar
  </button>

  <button @click="validarEscolhaProdutos" type="button"
    class="w-full sm:w-2/3 py-4 bg-blue-600
    text-white rounded-xl hover:bg-blue-500 transition-all">
    Próximo Passo
  </button>

</div>
        </div>

        <div v-if="etapa === 4" class="flex flex-col items-stretch gap-8 animate-fade-in w-full">

          <div class="bg-white/5 border border-white/10 rounded-2xl p-6">
            <h3 class="text-blue-400 text-sm tracking-widest uppercase mb-6 text-center">
              Produtos Selecionados
            </h3>
            <div class="space-y-4">
              <div v-for="item in itensFinal" :key="item.id" 
                class="flex justify-between items-center bg-slate-900/50 
                p-2 rounded-xl border border-white/5">
                <div class="flex flex-col">
                  <span class="text-white text-base font-medium mb-1">{{ item.nome_produto }}</span>
                  <span class="text-gray-400 text-sm">ID: {{ item.id }}</span>
                </div>
                <div class="text-right flex items-center
                  bg-blue-500/10 px-4 py-2 rounded-lg border border-blue-500/20">
                  <span class="text-blue-400 text-lg font-bold">{{ item.quantidadeDevolucao }}</span>
                  <span class="text-blue-400 text-sm">un.</span>
                </div>
              </div>
            </div>
          </div>

          <div class="flex flex-col group gap-3">
            <label class="text-blue-400/80 text-sm tracking-[0.2em] uppercase font-semibold">
              Estado do Produto
            </label>
            <select v-model="form.problema" class="p-5 rounded-xl bg-white/5 border border-white/10
              text-white focus:bg-slate-800 focus:ring-2 focus:ring-blue-500/50 
              outline-none transition-all cursor-pointer hover:border-white/20 appearance-none">
              <option value="" disabled class="bg-slate-900">Selecione o problema principal...</option>
              <option class="bg-slate-900">Quebrado</option>
              <option class="bg-slate-900">Amassado</option>
              <option class="bg-slate-900">Produto errado/marca errada</option>
              <option class="bg-slate-900">Referência errada (Similar, Genérico, etc...)</option>
              <option class="bg-slate-900">Outra...</option>
            </select>
          </div>

          <div class="flex flex-col gap-4">
            <h2 class="text-white text-xl font-medium">Detalhes da ocorrência</h2>
            <textarea v-model="form.descricao" rows="5" placeholder="Descreva os detalhes do problema..."
              class="w-full p-5 rounded-xl bg-white/5 border border-white/10
              text-white outline-none resize-none
              focus:border-blue-500 transition-all placeholder-gray-500">
            </textarea>
          </div>
          
          <label class="w-full flex items-center justify-center gap-4 p-8
            rounded-xl bg-white/5 border-2 border-dashed
            border-white/20 text-gray-400 cursor-pointer hover:border-blue-400 hover:text-blue-300 transition-all">
            <i class="fa-solid fa-cloud-arrow-up text-2xl"></i>
            <span class="truncate text-base font-medium">{{ arquivoNome || "Clique para anexar arquivo ou foto" }}</span>
            <input type="file" class="hidden" @change="selecionarArquivo">
          </label>

          <div class="flex flex-col-reverse sm:flex-row gap-4 mt-4 w-full">

  <button @click="etapa = 3" type="button"
    class="w-full sm:w-1/3 py-4 
    text-gray-400 hover:text-white hover:bg-white/5 
    rounded-xl transition-all font-medium">
    Voltar
  </button>

  <button type="button" @click="enviarFormularioSAC"
    class="w-full sm:w-2/3 py-4 bg-blue-600 hover:bg-blue-500
    text-white rounded-xl font-bold uppercase tracking-wider text-sm
    transition-all shadow-lg shadow-blue-500/25">
    Finalizar e Enviar
  </button>

</div>
        </div>
      </form>

      <div v-if="etapa === 5" class="animate-fade-in w-full">
        <FormSegundaViaNotaFiscal :cnpj="cnpj" :nota_fiscal="notaFiscal" />
        <button 
          type="button" 
          @click="etapa = 2" 
          class="mt-8 w-full py-4 border border-white/10
          text-gray-400 rounded-xl hover:bg-white/5 hover:text-white transition-all font-medium"
        >
          Voltar ao Início
        </button>
      </div>

      <div v-if="etapa === 6" class="animate-fade-in w-full">
        <FormSegundaViaBoleto :cnpj="cnpj"/>
        <button 
          type="button" 
          @click="etapa = 2" 
          class="mt-8 w-full py-4 border border-white/10
        text-gray-400 rounded-xl hover:bg-white/5 hover:text-white transition-all font-medium"
        >
          Voltar ao Início
        </button>
      </div>
    </div>
  </section>

<!-- Modal de identificação -->
  <Teleport to="body">
    <div v-if="mostrarModal" 
      class="fixed inset-0 flex items-center justify-center p-4 sm:p-6 bg-slate-950/80 backdrop-blur-md"
      style="z-index: 9999;">
      
      <div class="bg-slate-900 border border-white/10 p-8 sm:p-10 rounded-[2.5rem] w-full max-w-lg shadow-2xl animate-modal-in">
        <h3 class="text-white text-3xl font-bold text-center mb-8">Identificação</h3>
        
        <div class="space-y-6">
          <div class="flex flex-col gap-2">
            <label class="text-white/70 text-sm font-medium ml-1">Nome Completo</label>
            <input v-model="form.nome" type="text" placeholder="Ex: Rodrigo Fernandes..." class="w-full p-4
            rounded-xl bg-white/5 border border-white/10 text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all">
          </div>
          
          <div class="flex flex-col gap-2">
            <label class="text-white/70 text-sm font-medium ml-1">E-mail Corporativo</label>
            <input v-model="form.email" type="email" placeholder="Ex: contato@empresa.com" 
            class="w-full p-4 rounded-xl bg-white/5 border border-white/10 text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all">
          </div>

          <div class="flex flex-col gap-2">
            <label class="text-white/70 text-sm font-medium ml-1">WhatsApp / Telefone</label>
            <input v-model="form.contato" type="tel" placeholder="Ex: 5577999999999"
            class="w-full p-4 rounded-xl bg-white/5 border border-white/10 text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all">
          </div>
        </div>

        <div class="flex flex-col-reverse sm:flex-row gap-6 mt-10 w-full">
          <button type="button" @click="mostrarModal = false"
          class="w-full sm:w-1/3 py-4 text-gray-400 hover:text-white hover:bg-white/5 rounded-xl transition-all font-medium">
            Voltar
          </button>
          <button type="button" @click="iniciarVerificacao()" 
          class="w-full sm:w-2/3 py-4  text-white rounded-xl hover:bg-blue-500 transition-all">
            Avançar
          </button>
        </div>
      </div>
    </div>
  </Teleport>
  
<!-- Modal de confirmação de código-->
  <Teleport to="body">
    <div v-if="mostrarConfirmacao" 
      class="fixed inset-0 flex items-center justify-center p-4 sm:p-6 bg-slate-950/80 backdrop-blur-md"
      style="z-index: 9999;">
      
      <div class="bg-slate-900 border border-white/10 p-8 sm:p-10 rounded-[2.5rem] w-full max-w-lg shadow-2xl animate-modal-in">
        <div class="animate-fade-in flex flex-col gap-4">
          <h3 class="text-white text-3xl font-bold text-center mb-2">Verificação</h3>
          <p class="text-gray-400 text-center mb-6 leading-relaxed">
            Enviamos um código para o seu e-mail. Digite-o abaixo para continuar.
          </p>

          <input 
            v-model="codigoDigitado" 
            placeholder="Digite o código"
            class="w-full p-5 text-center text-xl tracking-[0.5em] rounded-xl bg-white/5 border border-white/10 text-white mb-6 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all" 
          />

          <button 
            type="button"
            @click="validarEmailEnviado" 
            class="w-full py-4 font-medium bg-green-600 text-white rounded-xl hover:bg-green-500 transition-all shadow-lg shadow-green-500/20">
            Validar Código
          </button>

          <div class="w-full h-px bg-white/10 my-4"></div>

          <button 
            type="button"
            @click="confirmarEmail" 
            class="w-full py-4 bg-white/5 text-blue-400 rounded-xl hover:bg-white/10 transition-all text-sm font-medium">
            Não recebi. Reenviar código 🔁
          </button>
        
          <button
            type="button" 
            @click="mostrarConfirmacao = false; mostrarModal = true"
            class="w-full mt-2 py-4 text-gray-500 hover:text-white rounded-xl transition-all font-medium">
            Voltar
          </button>
        </div>
      </div>
    </div>
  </Teleport>
<!-- Modal da nota fiscal-->
  <Teleport to="body">
    <div v-if="mostrarNotaFiscal"
      class="fixed inset-0 flex items-center justify-center p-4 sm:p-6 bg-slate-950/80 backdrop-blur-md"
      style="z-index: 9999;">
      
      <div class="bg-slate-900 border border-white/10 p-8 sm:p-10 rounded-[2.5rem] w-full max-w-lg shadow-2xl animate-modal-in">
        
        <h2 class="text-white text-2xl font-bold text-center mb-4 leading-snug">
          Identifique a Nota Fiscal
        </h2>
        <p class="text-gray-400 text-center text-sm mb-8">
          Digite o número para selecionarmos os itens a devolver.
        </p>

        <input 
          v-model="notaFiscal" 
          @blur="formatarNotaFiscal"
          placeholder="Ex: 000123"
          class="w-full p-5 text-xl font-medium tracking-widest rounded-xl bg-white/5 border border-white/10 text-white text-center mb-8 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all"
        >

        <div class="flex flex-col-reverse sm:flex-row gap-2 w-full">
          <button 
            type="button"
            @click="mostrarNotaFiscal = false; mostrarConfirmacao = true"
            class="w-full sm:w-1/2 py-2 text-gray-400 hover:text-white hover:bg-white/5 rounded-xl transition-all font-medium">
            Voltar
          </button>

          <button 
            type="button"
            @click="validarNotaFiscal"
            class="w-full sm:w-2/2 py-2 text-white rounded-xl hover:bg-blue-500 transition-all">
            Buscar Itens
          </button>
        </div>
      </div>
    </div>
  </Teleport>
</div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { criar_formulario_sac, enviarCodigo,validarCNPJ,validarCodigo,validar_cnpj_no_banco, validar_nota_fiscal }
from '../services/api';
import FormSegundaViaBoleto from '../components/FormSegundaViaBoleto.vue';
import FormSegundaViaNotaFiscal from '../components/FormSegundaViaNotaFiscal.vue';

const mostrarNotaFiscal = ref(false);
const mostrarConfirmacao = ref(false);
const codigoDigitado = ref('');
const etapa = ref(1);
const mostrarModal = ref(false);
const cnpj = ref('');
const cnpjValidado = ref(false);
const notaFiscal = ref('');
const arquivoNome = ref("");
const arquivo = ref(null);


const assuntos = {
  "Devolver Mercadoria": {
    imagem: "/devolucao.png",
    descricao: "Inicie o processo de logística reversa para produtos com defeito ou desistência."
  },
  "Segunda Via - Nota Fiscal": {
    imagem: "/segunda-via-notafiscal.png",
    descricao: "Recupere o arquivo XML ou PDF da sua nota fiscal de compra."
  },
  "Segunda Via - Boleto": {
    imagem: "/segunda-via-boleto.png",
    descricao: "Gere um novo boleto atualizado para pagamento imediato."
  },
  "Outros motivos....": {
    imagem: "/outros.png",
    descricao: "Fale com nossa equipe sobre qualquer outro assunto não listado acima."
  }
};

const itensNota = ref([]);
const itensSelecionados = ref([]);
const itensFinal = ref([]);

const form = reactive({
  assunto: 'Devolver Mercadoria',
  nome: '',
  contato: '',
  email: '',
  problema: '', // estado do produto
  situacao: 'enviado', // 
  notafiscal: '',
  descricao: '',
});


async function iniciarVerificacao() {
  if (!form.nome || !form.email || !form.contato) {
    alert("Preencha todos os campos (Nome, E-mail e WhatsApp)!🚨🚨🚨");
    return;
  }

  if (!form.email.includes("@")) {
    alert("E-mail inválido!🚨🚨🚨");
    return;
  }

  if (form.contato.length < 10) {
    alert("WhatsApp inválido!🚨🚨🚨");
    return;
  }
  mostrarModal.value = false;
  mostrarConfirmacao.value = true;

  await confirmarEmail();
}

async function validarCNPJDaEmpresa() {
  const cnpjLimpo = cnpj.value.replace(/\D/g, '');

  try {

    const res = await validarCNPJ(cnpjLimpo);
    console.log("API validação externa:", res);

    if (!res.valido && res.ok === false) {
      alert("Este CNPJ não é válido na Receita Federal 🚨");
      return; 
    }

    const res2 = await validar_cnpj_no_banco(cnpjLimpo);
    console.log("Resultado Banco:", res2);

    if (res2 && res2.existe) {
      cnpjValidado.value = true;
      etapa.value = 2;
      alert("CNPJ encontrado ✅")
    } else {
      alert("CNPJ válido, mas não encontrado no nosso banco 🚨");
    }

  } catch (error) {
    if (error.response && error.response.status === 404) {
      console.error("Erro: A rota no servidor não foi encontrada (404).");
    }
    alert("Erro ao processar validação. Verifique o console.");
  }
}

function formatarNotaFiscal(){
  notaFiscal.value = notaFiscal.value
  .replace(/\D/g, '')
  .slice(0, 6)
  .padStart(6 , '0');
}

async function validarNotaFiscal() {
  if (notaFiscal.value.length < 6) {
    alert("Nota fiscal inválida 🚨");
    return;
  }

  try {
    const res = await validar_nota_fiscal(notaFiscal.value);

    console.log(res);

    if (!res.existe) {
      alert("Nota não encontrada 🚨");
      return;
    }

    if (!res.itens || res.itens.length === 0) {
      alert("Nota sem itens 🚨");
      return;
    }

    itensNota.value = res.itens.map(item => ({...item,quantidadeDevolucao: 1}));
    mostrarNotaFiscal.value = false;
    etapa.value = 3;

  } catch (error) {
    console.error(error);
    alert("Erro ao buscar nota 🚨");
  }
}

async function validarEmailEnviado() {
  try {
    const res = await validarCodigo(form.email, codigoDigitado.value);

    if (res.valido) {
      alert("Código válido ✅");
      mostrarConfirmacao.value = false;
      if (form.assunto === "Devolver Mercadoria") {
        mostrarNotaFiscal.value = true;
      } 
      else if (form.assunto === "Segunda Via - Nota Fiscal") {
        etapa.value = 5; 
      } 
      else if (form.assunto === "Segunda Via - Boleto") {
        etapa.value = 6;
      } 
      else if (form.assunto === "Outros motivos....") {
        const fone = "08009980367";
        const mensagem = encodeURIComponent("Olá, gostaria de falar com o SAC sobre um problema.");
        window.location.href = `https://wa.me/${fone}?text=${mensagem}`;
      }
    } else {
      alert("Código inválido 🚨");
    }
  } catch (error) {
    console.error("Erro na validação:", error);
    alert("Erro técnico ao validar código.");
  }
}

async function confirmarEmail() {
  const res = await enviarCodigo(form.email);
  console.log(res);
  if (res.ok) {
    alert("Código enviado para o e-mail 📩"); 
  } else {
    alert("Erro ao enviar código, Verifique os campos 🚨");
  }
}



function validarEscolhaProdutos() {
  if (itensSelecionados.value.length === 0) {
    alert("Selecione pelo menos um produto 🚨");
    return;
  }
  for (const item of itensSelecionados.value) {
    if (!item.quantidadeDevolucao || item.quantidadeDevolucao < 1) {
      alert(`Informe a quantidade para ${item.nome_produto}`);
      return;
    }

    if (item.quantidadeDevolucao > item.quantidade) {
      alert(`Quantidade inválida para ${item.nome_produto}`);
      return;
    }
  }

  itensFinal.value = itensSelecionados.value.map(item => ({
  id: item.id,
  nome_produto: item.nome_produto,
  quantidade_original: item.quantidade,
  quantidade_devolucao: item.quantidadeDevolucao
  }));

  etapa.value = 4;
}

function selecionarArquivo(event) {
  const file = event.target.files[0];
  if (file) {
    arquivo.value = file;
    arquivoNome.value = file.name;
  }
}

function formatarCnpj() {
  let value = cnpj.value.replace(/\D/g, '').slice(0, 14);
  if (value.length > 2) value = value.replace(/^(\d{2})(\d)/, '$1.$2');
  if (value.length > 5) value = value.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
  if (value.length > 8) value = value.replace(/\.(\d{3})(\d)/, '.$1/$2');
  if (value.length > 12) value = value.replace(/\/(\d{4})(\d)/, '/$1-$2');
  cnpj.value = value;
}

async function enviarFormularioSAC() {
  try {
    const res = await criar_formulario_sac(
      {
        nome: form.nome,
        email: form.email,
        contato: form.contato,
        nota_fiscal: notaFiscal.value,
        assunto: form.assunto,
        problema: form.problema,
        descricao: form.descricao,
        itens: itensFinal.value.map(item => ({
          id: item.id,
          nome_produto: item.nome_produto,
          quantidade_original: item.quantidade_original,
          quantidade_devolucao: item.quantidade_devolucao
        }))
      },
      arquivo.value
    );
    console.log(res);
    Object.assign(form, { assunto: '', nome: '', contato: '', email: '', problema: '', descricao: '' });
    itensSelecionados.value = [];
    itensFinal.value = [];
    cnpj.value = '';
    arquivo.value = null;
    arquivoNome.value = "";
    etapa.value = 1;
    alert("Solicitação enviada pro SAC ✅");
    etapa.value = 1;
  } catch (error) {
    console.error(error);
    alert("Erro ao enviar para o SAC ❌");
  }
}

</script>


<style scoped>
/*ANIMAÇÂO DO MODAL*/

.animate-fade-in {
  animation: fadeIn 0.3s ease-in-out;
}

.animate-modal-in {
  animation: modalIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes modalIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}
</style>