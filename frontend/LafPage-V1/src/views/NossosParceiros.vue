<template>
  <div class="w-full h-12"></div>

  <div class="w-full flex flex-col items-center justify-center h-auto md:px-24 md:py-20 mb-10 px-6">
    <div class="relative group">
      <div class="absolute -inset-1 bg-gradient-to-r rounded-3xl blur opacity-20"></div>
      <h1 class="relative flex items-center gap-4 text-center text-4xl md:text-8xl lg:text-9xl
        bg-gradient-to-r from-blue-600 to-sky-400 bg-clip-text text-transparent
        font-black tracking-tighter px-8 py-4 bg-white/5 backdrop-blur-xl
        border border-white/10 rounded-[1rem] shadow-2xl">
        <i class="fa-solid fa-headset text-blue-500/40 text-4xl md:text-6xl"></i>
        SAC
      </h1>
    </div>

    <p class="mt-6 text-gray-400 text-base md:text-xl max-w-xl text-center leading-relaxed">
      Preencha os dados abaixo. Nossa equipe retornará o contato para 
      <span class="text-blue-400 font-medium">ajudá-lo</span> o mais rápido possível.
    </p>
  </div>

  <section class="w-full flex items-center justify-center pb-20 px-4">
    <div class="w-full max-w-[900px] bg-slate-900/60 backdrop-blur-2xl
      border border-white/10 rounded-[2.5rem]
      shadow-[0_20px_50px_rgba(0,0,0,0.3)] p-6 md:p-12 overflow-hidden">
      
      <form class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8 mt-6" 
      @submit.prevent="enviarFormularioSAC">

        <div class="flex flex-col md:col-span-2 group">
          <label class="text-blue-400/80 text-xs text-center tracking-[0.2em] uppercase mb-3 ml-1">
            Assunto Principal
          </label>
          <select v-model="form.assunto" class="p-4 rounded-2xl bg-white/5 border border-white/10
           text-white focus:bg-slate-800 focus:ring-2 focus:ring-blue-500/50 
           outline-none transition-all cursor-pointer hover:border-white/20">
            <option class="bg-slate-900">Devolver Mercadoria</option>
            <option class="bg-slate-900">Segunda Via - Boleto</option>
            <option class="bg-slate-900">Segunda Via - Nota Fiscal</option>
            <option class="bg-slate-900">Outros motivos....</option>
          </select>
        </div>

        <div class="flex flex-col">
          <label class="text-gray-400 text-sm mb-2 ml-1">Nome Completo</label>
          <input v-model="form.nome" type="text" placeholder="Como podemos te chamar?" required
            class="p-4 rounded-2xl bg-white/5 border border-white/10 text-white
             placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50
              outline-none transition-all hover:border-white/20">
        </div>

        <div class="flex flex-col">
          <label class="text-gray-400 text-sm mb-2 ml-1">WhatsApp / Telefone</label>
          <input v-model="form.contato" type="tel" placeholder="(00) 00000-0000" required
            class="p-4 rounded-2xl bg-white/5 border border-white/10
             text-white placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50
              outline-none transition-all hover:border-white/20">
        </div>

        <div class="flex flex-col">
          <label class="text-gray-400 text-sm mb-2 ml-1">E-mail</label>
          <input v-model="form.email" type="email" placeholder="exemplo@email.com" required
            class="p-4 rounded-2xl bg-white/5 border border-white/10
             text-white placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50 
             outline-none transition-all hover:border-white/20">
        </div>

        <div class="flex flex-col">
          <label class="text-gray-400 text-sm mb-2 ml-1">Data da Ocorrência</label>
          <input v-model="form.data" type="date" required
            class="p-4 rounded-2xl bg-white/5 border border-white/10 text-white
             focus:ring-2 focus:ring-blue-500/50 outline-none transition-all 
             [color-scheme:dark] hover:border-white/20">
        </div>

        <div class="flex flex-col">
          <label class="text-gray-400 text-sm mb-2 ml-1">Número da Nota Fiscal</label>
          <input v-model="form.notafiscal" type="text" inputmode="numeric" placeholder="Opcional"
            class="p-4 rounded-2xl bg-white/5 border border-white/10
             text-white placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50
              outline-none transition-all hover:border-white/20">
        </div>

        <div class="flex flex-col">
          <label class="text-gray-400 text-sm mb-2 ml-1">CNPJ da Empresa</label>
          <input v-model="cnpj" @input="formatarCnpj" maxlength="18"
            placeholder="00.000.000/0000-00"
            class="p-4 rounded-2xl bg-white/5 border border-white/10 text-white
             placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50 outline-none
              transition-all hover:border-white/20">
        </div>
        
        <div class="flex flex-col md:col-span-2">
          <label class="text-gray-400 text-sm mb-2 ml-1 text-center">
            Anexar imagem ou documento (Opcional)
          </label>
          <label class="flex items-center justify-center gap-3 p-5 rounded-2xl
            bg-white/5 border border-dashed border-white/20
            text-gray-400 cursor-pointer hover:border-blue-400 transition-all">
            <i class="fa-solid fa-paperclip text-blue-400"></i>
            <span>{{ arquivoNome || "Clique para anexar imagem ou documento" }}</span>
            <input type="file" class="hidden" accept=".jpg,.jpeg,.png,.pdf,.doc,.docx"
              @change="selecionarArquivo">
          </label>
        </div>

        <div class="flex flex-col md:col-span-2">
          <label class="text-gray-400 text-sm text-center mb-2 ml-1">
            Detalhes do seu problema
          </label>
          <textarea v-model="form.detalhe" rows="4" required
            placeholder="Conte-nos o que aconteceu em detalhes..." 
            class="p-5 rounded-3xl bg-white/5 border border-white/10
             text-white placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50 outline-none 
             transition-all resize-none hover:border-white/20"></textarea>
        </div>

        <div class="md:col-span-2 pt-6">
            <button type="submit" :disabled="enviado"
             class="w-full py-5 rounded-2xl transition-all duration-300 shadow-xl
             flex items-center justify-center gap-3 text-white"
             :class="enviado 
               ? 'bg-green-600 cursor-default' 
               : 'bg-gradient-to-r from-blue-600 to-sky-500 hover:from-sky-400 hover:to-indigo-500 shadow-blue-900/20'">
            <i v-if="!enviado" class="fa-solid fa-paper-plane"></i>
            <i v-else class="fa-regular fa-circle-check text-green-200"></i>
            <span>{{ enviado ? "SOLICITAÇÃO ENVIADA" : "ENVIAR SOLICITAÇÃO AGORA" }}</span>
            </button>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from 'vue';

const cnpj = ref('');
const enviado = ref(false);
const arquivo = ref(null);
const arquivoNome = ref("");

const form = reactive({
  assunto: 'Devolver Mercadoria',
  nome: '',
  contato: '',
  email: '',
  data: '',
  notafiscal: '',
  detalhe: '', 
})

function formatarCnpj() {
  let value = cnpj.value.replace(/\D/g, '').slice(0, 14);
  
  if (value.length > 2) value = value.replace(/^(\d{2})(\d)/, '$1.$2');
  if (value.length > 6) value = value.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
  if (value.length > 10) value = value.replace(/\.(\d{3})(\d)/, '.$1/$2');
  if (value.length > 14) value = value.replace(/(\d{4})(\d)/, '$1-$2');

  cnpj.value = value;
}

function selecionarArquivo(event){
  const file = event.target.files[0];
  if(file){
    arquivo.value = file;
    arquivoNome.value = file.name;
  }
}

function enviarFormularioSAC(){
  const dadosParaEnvioSAC = { ...form, cnpj: cnpj.value, arquivo: arquivo.value };
  console.log("Enviando SAC:", dadosParaEnvioSAC);
  
  enviado.value = true;
  
  setTimeout(() => { enviado.value = false; }, 5000);
}
</script>