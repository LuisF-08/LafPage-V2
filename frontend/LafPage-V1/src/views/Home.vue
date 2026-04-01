<script setup>
import Carrosel from '../components/Carrosel.vue';
import TelaTelevendas from '../components/TelaTelevendas.vue';
import SobreNos from '../components/SobreNos.vue';
import CarroselParceiros from '../components/CarroselParceiros.vue';
import bg from '../assets/capa-site-lafmed.png'
import Institucional from '../components/Institucional.vue';

const fone = "558005910367";
const mensagem = encodeURIComponent("Olá, gostaria de verificar as promoções!.");
const linkWhatsApp = `https://wa.me/${fone}?text=${mensagem}`;
</script>

<template>

  <!-- BACKGROUND -->
  <div
    class="fixed inset-0 -z-10"
    :style="{ backgroundImage: `url(${bg})` }"
  >
    <div class="absolute inset-0 bg-cover bg-center blur-xl scale-110"></div>
  </div>

  <!-- OVERLAY VIDRO -->
  <div class="fixed inset-0 -z-10 bg-black/30 backdrop-blur-md"></div>

  <!-- CONTEÚDO -->
  <div class="flex flex-col gap-20 pb-20 w-full overflow-x-hidden">

   <!--BOTÂO FIXO DO WHATSAPP-->
  <a 
  :href="linkWhatsApp"
  target="_blank"
  class="fixed bottom-8 right-8 bg-green-500 text-white
  w-20 h-20 flex items-center justify-center rounded-full
  shadow-[0_10px_25px_rgba(34,197,94,0.4)] hover:bg-green-600 hover:scale-110
  transition-all duration-300 group z-[9999]"
  title="Fale com a gente!"
>
  <i class="fa-brands fa-whatsapp text-5xl"></i>

  <span class="absolute inline-flex h-full w-full rounded-full 
  bg-green-400 opacity-75 animate-ping -z-50"></span>
</a>

    <!-- templates  responsável por todas essa parte visual
     indo do institucional -> promoções -> conversar com televendas -> localização e estatistica e
     os pareceiros escolhidos -->

    <Institucional />
    
    <Carrosel />

    <TelaTelevendas />

    <SobreNos />

    <CarroselParceiros />

  </div>

</template>