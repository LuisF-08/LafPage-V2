<script setup>
import bg from '../assets/capa-site-lafmed.png'
import FormSAC from '../components/FormSAC.vue';

const fone = "08009980367";

const mensagem = encodeURIComponent("Olá, gostaria de reltar um problema!.");
const linkWhatsApp = `https://wa.me/${fone}?text=${mensagem}`;

</script>

<template>
  <div class="fixed inset-0 -z-10">
    <div 
      class="absolute inset-0 bg-cover bg-center blur-xl scale-110"
      :style="{ backgroundImage: `url(${bg})` }"
    ></div>
    <div class="absolute inset-0 bg-black/40 backdrop-blur-md"></div>
  </div>

  <main class="relative min-h-screen w-full overflow-x-hidden pt-40 pb-20 flex flex-col items-center">
    
    <FormSAC />

    <a 
      :href="linkWhatsApp"
      target="_blank"
      class="fixed bottom-8 right-8 bg-green-500 text-white
             w-20 h-20 flex items-center justify-center rounded-full
             shadow-[0_10px_25px_rgba(34,197,94,0.4)] hover:bg-green-600 hover:scale-110
             transition-all duration-300 group z-[9999]"
      title="Fale com nosso SAC!"
    >
      <i class="fa-brands fa-whatsapp text-5xl"></i>
      <span class="absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75 animate-ping -z-10"></span>
    </a>
  </main>
</template>

<style scoped>
/* Garante que o scroll seja suave */
html {
  scroll-behavior: smooth;
}
</style>