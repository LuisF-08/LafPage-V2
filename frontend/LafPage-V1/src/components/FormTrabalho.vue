<template>
  <div class="w-full h-12"></div>

  <div class="w-full flex flex-col items-center justify-center h-auto md:px-24 md:py-20 mb-10 px-6">
    
    <div class="relative group">
      <div class="absolute -inset-1 bg-gradient-to-r rounded-3xl blur opacity-20"></div>

      <h1 class="relative flex items-center gap-3 text-center text-4xl md:text-8xl lg:text-9xl
        bg-gradient-to-r from-blue-600 to-sky-400 bg-clip-text text-transparent
        font-black tracking-tighter px-8 py-4 bg-white/5 backdrop-blur-xl
        border border-white/10 rounded-[1rem] shadow-2xl">
        <i class="fa-solid fa-building-user"></i>
        TRABALHE CONOSCO
      </h1>
    </div>

    <p class="mt-6 text-gray-400 text-base md:text-xl max-w-xl text-center leading-relaxed">
      Preencha as informações abaixo. Iremos avaliar a compatibilidade com a vaga
      e, caso esteja de acordo com o perfil que buscamos, retornaremos o contato para 
      contratá-lo o mais rápido possível!
    </p>

  </div>

  <section class="w-full flex items-center justify-center pb-20 px-4">

    <div class="w-full max-w-[900px] bg-slate-900/60 backdrop-blur-2xl
      border border-white/10 rounded-[2.5rem]
      shadow-[0_20px_50px_rgba(0,0,0,0.3)] p-6 md:p-12 overflow-hidden">
      
      <form class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8 mt-6" 
      @submit.prevent="enviarFormularioTrabalho">

        <div class="flex flex-col md:col-span-2 group">
          <label class="text-blue-400/80 text-xs text-center tracking-[0.2em] uppercase mb-3 ml-1">
            Vaga
          </label>
          <select v-model="form.vaga" class="p-4 rounded-2xl bg-white/5 border border-white/10
            text-white focus:bg-slate-800 focus:ring-2 focus:ring-blue-500/50 
            outline-none transition-all cursor-pointer hover:border-white/20">
            <option value="" disabled class="bg-slate-900">Selecione uma vaga</option>
            <option class="bg-slate-900">Logística</option>
            <option class="bg-slate-900">Administrativo</option>
            <option class="bg-slate-900">Geral</option>
            <option class="bg-slate-900">Televendas</option>
            <option class="bg-slate-900">Outra...</option>
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
          <label class="text-gray-400 text-sm mb-2 ml-1">Gênero</label>
          <input v-model="form.genero" type="text" placeholder="Como se identifica?" required
            class="p-4 rounded-2xl bg-white/5 border border-white/10 text-white
             placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50
              outline-none transition-all hover:border-white/20">
        </div>

        <div class="flex flex-col md:col-span-2 group">
          <label class="text-blue-400/80 text-xs text-center tracking-[0.2em] uppercase mb-3 ml-1">
           Faixa etária
          </label>
          <select v-model="form.faixaEtaria" class="p-4 rounded-2xl bg-white/5 border border-white/10
            text-white focus:bg-slate-800 focus:ring-2 focus:ring-blue-500/50 
            outline-none transition-all cursor-pointer hover:border-white/20">
            <option class="bg-slate-900">16-18</option>
            <option class="bg-slate-900">18-30</option>
            <option class="bg-slate-900">30-50+</option>
          </select>
        </div>

        <div class="flex flex-col">
          <label class="text-gray-400 text-sm mb-2 ml-1">Endereço</label>
          <input v-model="form.endereco" type="text" placeholder="Rua/Avenida, Bairro, Cidade" required
            class="p-4 rounded-2xl bg-white/5 border border-white/10
             text-white placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50 
             outline-none transition-all hover:border-white/20">
        </div>

        <div class="flex flex-col">
          <label class="text-gray-400 text-sm mb-2 ml-1">CEP</label>
          <input v-model="cep" @input="formatarCep" maxlength="9"
            placeholder="00000-000"
            class="p-4 rounded-2xl bg-white/5 border border-white/10 text-white
             placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50 outline-none
              transition-all hover:border-white/20">
        </div>

        <div class="flex flex-col">
          <label class="text-gray-400 text-sm mb-2 ml-1">WhatsApp / Telefone</label>
          <input v-model="form.telefone" type="tel" placeholder="(00) 00000-0000" required
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
          <label class="text-gray-400 text-sm mb-2 ml-1">Data de Nascimento</label>
          <input v-model="form.dataNascimento" type="date" required
            class="p-4 rounded-2xl bg-white/5 border border-white/10 text-white
             focus:ring-2 focus:ring-blue-500/50 outline-none transition-all 
             [color-scheme:dark] hover:border-white/20">
        </div>
 
        <div class="flex flex-col md:col-span-2">
          <label class="text-gray-400 text-sm mb-2 ml-1 text-center">
            Anexar imagem ou documento
          </label>
          <label class="flex items-center justify-center gap-3 p-5 rounded-2xl
            bg-white/5 border border-dashed border-white/20
            text-gray-400 cursor-pointer hover:border-blue-400
            transition-all">
            <i class="fa-solid fa-paperclip text-blue-400"></i>
            <span v-if="!arquivoNome">
              Clique para anexar Currículo ou Portfólio
            </span>
            <span v-else class="text-green-400">
              {{ arquivoNome }}
            </span>
            <input type="file" class="hidden" accept=".jpg,.jpeg,.png,.pdf,.doc,.docx"
              @change="selecionarArquivo">
          </label>
        </div>

        <div class="flex flex-col md:col-span-2 group">
          <label class="text-blue-400/80 text-xs text-center tracking-[0.2em] uppercase mb-3 ml-1">
            Nível de escolaridade
          </label>
          <select v-model="form.escolaridade" class="p-4 rounded-2xl bg-white/5 border border-white/10
            text-white focus:bg-slate-800 focus:ring-2 focus:ring-blue-500/50 
            outline-none transition-all cursor-pointer hover:border-white/20">
            <option class="bg-slate-900">Fundamental</option>
            <option class="bg-slate-900">Médio/Técnico</option>
            <option class="bg-slate-900">Superior</option>
            <option class="bg-slate-900">Outro....</option>
          </select>
        </div>

        <div class="flex flex-col md:col-span-2">
          <label class="text-gray-400 text-center text-sm mb-2 ml-1">Área/Curso de Formação</label>
          <input v-model="form.formacao" type="text" placeholder="Qual sua formação (se tiver)"
            class="p-4 rounded-2xl bg-white/5 border border-white/10 text-white
             placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50
              outline-none transition-all hover:border-white/20">
        </div>

        <div class="flex flex-col md:col-span-2">
          <label class="text-gray-400 text-sm text-center mb-2 ml-1">
            Experiência Profissional anterior
          </label>
          <textarea v-model="form.experiencia" rows="4"
            placeholder="Conte-nos em detalhes sua rotina, afazeres, cargo, etc..." 
            class="p-5 rounded-3xl bg-white/5 border border-white/10
             text-white placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50 outline-none 
             transition-all resize-none hover:border-white/20"></textarea>
        </div>

        <div class="flex flex-col md:col-span-2">
          <label class="text-gray-400 text-sm text-center mb-2 ml-1">
            Referência
          </label>
          <textarea v-model="form.referencia" rows="4"
            placeholder="Indicações e afins..." 
            class="p-5 rounded-3xl bg-white/5 border border-white/10
             text-white placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50 outline-none 
             transition-all resize-none hover:border-white/20"></textarea>
        </div>

        <div class="flex flex-col md:col-span-2">
          <label class="text-gray-400 text-sm text-center mb-2 ml-1">
            Habilidades e Competências
          </label>
          <textarea v-model="form.habilidades" rows="4" required
            placeholder="Nos fale sobre suas habilidades, personalidade, etc..." 
            class="p-5 rounded-3xl bg-white/5 border border-white/10
             text-white placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50 outline-none 
             transition-all resize-none hover:border-white/20"></textarea>
        </div>

        <div class="flex flex-col md:col-span-2 group">
          <label class="text-blue-400/80 text-xs text-center tracking-[0.2em] uppercase mb-3 ml-1">
           Carga Horária (Lembrando que temos 2H de almoço)
          </label>
          <select v-model="form.cargaHoraria" class="p-4 rounded-2xl bg-white/5 border border-white/10
            text-white focus:bg-slate-800 focus:ring-2 focus:ring-blue-500/50 
            outline-none transition-all cursor-pointer hover:border-white/20">
            <option class="bg-slate-900">8h-18h</option>
            <option class="bg-slate-900">10h-20h</option>
            <option class="bg-slate-900">Televendas 14h - 20h</option>
            <option class="bg-slate-900">Televendas 8h - 14h</option>
            <option class="bg-slate-900">Logística 9h - 20h</option>
            <option class="bg-slate-900">Logística 14h - 23:45h</option>
          </select>
        </div>

        <div class="flex flex-col md:col-span-2">
          <label class="text-gray-400 text-sm text-center mb-2 ml-1">
            Por que deseja trabalhar com nossa equipe?
          </label>
          <textarea v-model="form.motivo" rows="4"
            placeholder="Descreva o motivo de querer entrar para a LAFMED" 
            class="p-5 rounded-3xl bg-white/5 border border-white/10
             text-white placeholder-gray-600 focus:ring-2 focus:ring-blue-500/50 outline-none 
             transition-all resize-none hover:border-white/20"></textarea>
        </div>

        <div class="md:col-span-2 pt-6">
            <button
             type="submit"
             class="w-full py-5 rounded-2xl transition-all duration-300 shadow-xl
             flex items-center justify-center gap-3 text-white"
             :class="enviado 
               ? 'bg-green-600 shadow-green-900/20' 
               : 'bg-gradient-to-r from-blue-600 to-sky-500 hover:from-sky-400 hover:to-indigo-500 shadow-blue-900/20'
            ">
            <i v-if="!enviado" class="fa-solid fa-paper-plane"></i>
            <i v-else class="fa-regular fa-circle-check text-green-200"></i>
            <span>
              {{ enviado ? "SOLICITAÇÃO ENVIADA" : "ENVIAR SOLICITAÇÃO AGORA" }}
            </span>
            </button>
        </div>

      </form>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from 'vue';

const enviado = ref(false);
const cep = ref('');
const arquivo = ref(null);
const arquivoNome = ref('');

// Objeto para agrupar os campos
const form = reactive({
  vaga: '',
  nome: '',
  genero: '',
  faixaEtaria: '18-30',
  endereco: '',
  telefone: '',
  email: '',
  dataNascimento: '',
  escolaridade: 'Médio/Técnico',
  formacao: '',
  experiencia: '',
  referencia: '',
  habilidades: '',
  cargaHoraria: '8h-18h',
  motivo: ''
});

function formatarCep() {
  let value = cep.value.replace(/\D/g, '').slice(0, 8);
  if (value.length > 5) {
    value = value.replace(/^(\d{5})(\d+)/, '$1-$2');
  }
  cep.value = value;
}

function selecionarArquivo(event) {
  const file = event.target.files[0];
  if (file) {
    arquivo.value = file;
    arquivoNome.value = file.name;
  }
}

function enviarFormularioTrabalho() {
  const  dadosParaEnvioTrabalho = { ...form, cep: cep.value, arquivo: arquivo.value };
  console.log("Dados enviados:", dadosParaEnvioTrabalho);
  enviado.value = true;

  setTimeout(() => { enviado.value = false; }, 5000);
}
</script>