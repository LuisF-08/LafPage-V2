<template>
  <div class="w-full h-12"></div>

  <div class="w-full flex flex-col items-center justify-center h-auto md:px-24 md:py-20 mb-10 px-6">
    <div class="relative group">
      <div class="absolute -inset-1 bg-gradient-to-r from-blue-600 to-sky-400 rounded-xl blur opacity-20"></div>
      <h1 class="relative p-12 flex items-center gap-4 text-center text-4xl md:text-8xl lg:text-9xl
        bg-gradient-to-r from-blue-600 to-sky-400 bg-clip-text text-transparent
        font-black tracking-tighter md:py-12 px-8 py-4 bg-white/5 backdrop-blur-xl
        border border-white/10 rounded-xl shadow-2xl">
        <i class="fa-solid fa-headset text-blue-500/40 text-4xl md:text-6xl"></i>
        SAC
      </h1>
    </div>
    
    <div class="flex items-center gap-8 mt-12">
      <div v-for="i in 4" :key="i" 
        class="h-4 w-12 rounded-full transition-all duration-500"
        :class="etapa >= i ? 'bg-blue-500 shadow-[0_0_10px_rgba(59,130,246,0.5)]' : 'bg-white/10'">
      </div>
    </div>
  </div>

  <section class="w-full flex items-center justify-center pb-20 px-4">
    <div class="w-full max-w-[900px] bg-slate-900/60 backdrop-blur-2xl
      border border-white/10 rounded-[2.5rem]
      shadow-[0_20px_50px_rgba(0,0,0,0.3)] p-6 md:p-12 relative">
      
      <form class="grid grid-cols-1 gap-6 mt-6" @submit.prevent="enviarFormularioSAC">

        <div v-if="etapa === 1" class="flex flex-col items-center gap-6 w-full animate-fade-in">
            <h2 class="text-white text-2xl font-bold">Identificação</h2>
            <div class="flex flex-col w-full max-w-md">
              <input v-model="cnpj" @input="formatarCnpj"
               maxlength="18"
               placeholder="00.000.000/0000-00"
                class="p-4 rounded-2xl bg-white/5 border border-white/10
                 text-white text-center text-xl outline-none
                 focus:ring-2 focus:ring-blue-500/50 transition-all">
              <button 
                @click="validarCNPJDaEmpresa" type="button" 
                :disabled="cnpj.length < 18" class="mt-6 py-4 bg-blue-600
                 hover:bg-blue-500 disabled:opacity-30
                text-white rounded-2xl font-bold transition-all">
                     Continuar
                   </button>
            </div>
        </div>

    <div v-if="etapa === 2" class="flex flex-col animate-fade-in">
      <label class="text-blue-400 text-xs text-center
       tracking-[0.2em] uppercase mb-6">Selecione o Assunto</label>
      <div class="grid grid-cols-2 gap-3 mb-6">
        <button 
          v-for="(dados, label) in assuntos" 
          :key="label"
          @click="form.assunto = label"
          type="button"
          :class="[
            'flex flex-col items-center p-4 rounded-2xl border transition-all duration-300',
            form.assunto === label 
              ? 'border-blue-500 bg-blue-500/10 ring-1 ring-blue-500' 
              : 'border-white/10 bg-white/5 hover:bg-white/10'
          ]"
        >
          <img :src="dados.imagem" class="h-16 w-16 object-contain mb-3" :alt="label">
          <span class="text-white text-xs text-center leading-tight">{{ label }}</span>
        </button>
      </div>
    
      <div class="min-h-[80px] py-8"> <transition name="fade">
          <div 
            v-if="form.assunto" 
            class="bg-blue-500/10 border border-blue-500/20 p-6 rounded-xl mb-8 animate-fade-in"
          >
            <p class="text-blue-200 text-sm text-center italic">
              <span class="font-bold uppercase text-[10px] block mb-1">O que é isso?</span>
              "{{ assuntos[form.assunto].descricao }}"
            </p>
          </div>
        </transition>
      </div>

      <div class="flex gap-4">
        <button @click="etapa = 1" type="button" class="w-1/3 py-4 border border-white/10 text-gray-400 rounded-xl">Voltar</button>
        <button 
          @click="mostrarModal = true" 
          :disabled="!form.assunto"
          type="button" 
          class="w-2/3 py-4 bg-blue-600 text-white rounded-xl font-bold hover:bg-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
        >
          Próximo Passo
        </button>
      </div>
  </div>

        <div v-if="etapa === 3" class="flex flex-col gap-6 animate-fade-in">
          <h2 class="text-white text-2xl font-bold text-center">
            Itens da Nota Fiscal
          </h2>
          <div class="overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-300 border border-white/10 rounded-xl overflow-hidden">
              <thead class="bg-white/10 text-gray-400 uppercase text-xs">
                <tr>
                  <th class="p-3">Selecionar</th>
                  <th class="p-3">Produto</th>
                  <th class="p-3">Quantidade</th>
                  <th class="p-3">Valor</th>
                  <th class="p-3">Descricao</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in itensNota" :key="item.id" class="border-t border-white/10 hover:bg-white/5">
                  <td class="p-3 text-center">
                    <input type="checkbox" v-model="itensSelecionados" :value="item">
                  </td>
                  <td class="p-3">{{ item.nome }}</td>
                  <td class="p-3">{{ item.qtd }}</td>
                  <td class="p-3">R$ {{ item.valor }}</td>
                  <td class="p-3">{{ item.descricao }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="flex gap-4 mt-8">
            <button @click="etapa = 2" type="button"
              class="w-1/3 py-4 border border-white/10 text-gray-400 rounded-xl">
              Voltar
            </button>
            <button @click="validarEscolhaProdutos" type="button"
              class="w-2/3 py-4 bg-blue-600 text-white rounded-xl font-bold hover:bg-blue-500">
              Próximo Passo
            </button>
          </div>
        </div>

        <div v-if="etapa === 4" class="flex flex-col gap-6 animate-fade-in">
          <h2 class="text-white text-2xl font-bold text-center">Detalhes do pedido</h2>
          <textarea v-model="form.detalhe" rows="5" placeholder="Explique o motivo da devolução e demais assuntos..." 
            class="p-5 rounded-xl bg-white/5 border border-white/10 text-white outline-none resize-none focus:border-blue-500"></textarea>
          
          <label class="flex items-center justify-center gap-3 p-8 rounded-xl bg-white/5 border border-dashed
           border-white/20 text-gray-400 cursor-pointer hover:border-blue-400 transition-all">
            <i class="fa-solid fa-paperclip"></i>
            <span>{{ arquivoNome || "Anexar arquivo" }}</span>
            <input type="file" class="hidden" @change="selecionarArquivo">
          </label>

          <div class="flex gap-4 pt-6">
            <button @click="etapa = 3" type="button" class="w-1/3 py-5 border border-white/10 text-gray-400 rounded-2xl">Voltar</button>
            <button type="submit" class="w-2/3 py-5 bg-blue-600 hover:bg-blue-500 text-white rounded-2xl font-bold">FINALIZAR E ENVIAR</button>
          </div>
        </div>

      </form>
    </div>
  </section>

  <Teleport to="body">
    <div v-if="mostrarModal" 
      class="fixed inset-0 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md"
      style="z-index: 9999;">
      
      <div class="bg-slate-900 border border-white/20 p-8 rounded-[2.5rem] w-full max-w-lg shadow-2xl animate-modal-in">
        <h3 class="text-white text-2xl font-bold text-center mb-6">Identificação do Cliente</h3>
        
        <div class="space-y-4">
          <h2 class="text-white text-2xl  text-left mb-6">Nome</h2>
          <input v-model="form.nome" type="text" placeholder="Ex:Rodrigo Fernandes M...." class="w-full p-4 rounded-xl bg-white/5 border
           border-white/10 text-white focus:border-blue-500 outline-none">
           <h2 class="text-white text-2xl text-left mb-6">@Email</h2>
          <input v-model="form.email" type="email" placeholder="Ex: jhonstuart@gmail.com" class="w-full p-4 rounded-xl bg-white/5 border
           border-white/10 text-white focus:border-blue-500 outline-none">
           <h2 class="text-white text-2xl  text-left mb-6">Telefonel</h2>
          <input v-model="form.contato" type="tel" placeholder="Ex: 557723236750, tudo junto..." class="w-full p-4 rounded-xl bg-white/5 border
           border-white/10 text-white focus:border-blue-500 outline-none">
        </div>

        <div class="flex gap-4 mt-8">
          <button @click="mostrarModal = false" type="button" 
          class="w-1/3 py-4 text-gray-500 hover:text-white
           transition-all">Voltar</button>
          <button @click="iniciarVerificacao()" type="button" 
          class="w-2/3 py-4 bg-blue-600 text-white rounded-xl
           font-bold hover:bg-blue-500 transition-all">Avançar</button>
        </div>
      </div>
    </div>
  </Teleport>

  <Teleport to="body">
    <div v-if="mostrarConfirmacao" 
      class="fixed inset-0 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md"
      style="z-index: 9999;">
      
      <div class="bg-slate-900 border border-white/20 p-8 rounded-[2.5rem]
       w-full max-w-lg shadow-2xl animate-modal-in">
      <div class="animate-fade-in">
      <h3 class="text-white text-2xl font-bold text-center mb-6">
        Verificação por E-mail
      </h3>
    
      <p class="text-gray-400 text-center mb-6">
        Clique para enviar o código e depois digite abaixo:
      </p>
      <!-- BOTÃO ENVIAR EMAIL -->
      <button 
        @click="confirmarEmail" 
        type="button"
        class="w-full py-4 mb-4 bg-blue-600 text-white rounded-xl font-bold hover:bg-blue-500">
        Enviar Código
      </button>
    
      <!-- INPUT DO CÓDIGO -->
      <input 
        v-model="codigoDigitado" 
        placeholder="Digite o código recebido"
        class="w-full p-4 rounded-xl bg-white/5 border border-white/10 text-white mb-4" 
      />
      <!-- BOTÃO VALIDAR -->
      <button 
        @click="validarEmailEnviado" 
        type="button"
        class="w-full py-4 bg-green-600 text-white rounded-xl font-bold hover:bg-green-500">
        Validar Código
      </button>
    
      <!-- VOLTAR -->
      <button 
        @click="mostrarConfirmacao = false; mostrarModal = true"
        type="button"
        class="w-full mt-4 py-3 text-gray-500 hover:text-white transition-all">
        Voltar
      </button>
    </div>

      </div>
    </div>
  </Teleport>

</template>

<script setup>
import { ref, reactive } from 'vue';
import { enviarCodigo,validarCNPJ,validarCodigo } from '../services/api';

const autenticacao = ref(false);
const mostrarConfirmacao = ref(false);
const codigoDigitado = ref('');
const etapa = ref(1);
const mostrarModal = ref(false);
const cnpj = ref('');
const cnpjValidado = ref(false);
const arquivoNome = ref("");

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
const itensNota = ref([
  { id: 1, nome: 'Produto A', qtd: 2, valor: 150, descricao: 'apenas um teste de funcionamento' },
  { id: 2, nome: 'Produto B', qtd: 1, valor: 80 , descricao: 'apenas um teste de funcionamento'},
  { id: 3, nome: 'Produto C', qtd: 5, valor: 40 , descricao: 'apenas um teste de funcionamento'}
]);

const itensSelecionados = ref([]);

const form = reactive({
  assunto: 'Devolver Mercadoria',
  nome: '',
  contato: '',
  email: '',
  notafiscal: '',
  detalhe: '',
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
  autenticacao.value = false; 

  await confirmarEmail();
}

async function validarCNPJDaEmpresa() {
  if (cnpj.value.length < 18) {
    alert("Preencha um CNPJ completo 🚨");
    return;
  }
  try {
    const cnpjLimpo = cnpj.value.replace(/\D/g, ''); 
    const res = await validarCNPJ(cnpjLimpo); 
    console.log("Resposta da API:", res);
    if (res && (res.ok || res.valid || res.status === 200)) { 
      cnpjValidado.value = true;
      alert("CNPJ válido ✅");
      etapa.value = 2;
    } else {
      alert("CNPJ inválido ou não encontrado na base 🚨");
    }
  } catch (error) {
    alert("Erro de conexão ou servidor ao validar CNPJ 🚨");
    console.error(error);
  }
}

async function validarEmailEnviado() {
  const res = await validarCodigo(form.email, codigoDigitado.value);

  console.log(res);

  if (res.valido) {
    alert("Código válido ✅");
    mostrarConfirmacao.value = false;
    etapa.value = 3; 
  } else {
    alert("Código inválido 🚨");
  }
}

async function confirmarEmail() {
  const res = await enviarCodigo(form.email);
  console.log(res);
  if (res.ok) {
    alert("Código enviado para o e-mail 📩");
    autenticacao.value = false; 
  } else {
    alert("Erro ao enviar código 🚨");
  }
}

//async function enviar() {
//  const res = await enviarCodigo(form.email);
//  if (res.ok) {
//    mostrarConfirmacao.value = true;
//  }
//}
//
//function validarNotaEIrParaProdutos() {
//  if (!form.notafiscal) {
//    alert("Preencha o número da Nota Fiscal!🚨🚨🚨");
//    return;
//  }
//  mostrarConfirmacao.value = false;
//  etapa.value = 3; 
//}
//
function validarEscolhaProdutos() {
  if (itensSelecionados.value.length === 0) {
    alert("Selecione pelo menos um produto 🚨");
    return;
  }
  etapa.value = 4;
}

function selecionarArquivo(event) {
  const file = event.target.files[0];
  if (file) arquivoNome.value = file.name;
}

function formatarCnpj() {
  let value = cnpj.value.replace(/\D/g, '').slice(0, 14);
  if (value.length > 2) value = value.replace(/^(\d{2})(\d)/, '$1.$2');
  if (value.length > 5) value = value.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
  if (value.length > 8) value = value.replace(/\.(\d{3})(\d)/, '.$1/$2');
  if (value.length > 12) value = value.replace(/\/(\d{4})(\d)/, '/$1-$2');
  cnpj.value = value;
}

function enviarFormularioSAC() {
  alert("Solicitação enviada!");
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