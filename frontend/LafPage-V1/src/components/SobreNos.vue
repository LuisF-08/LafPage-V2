<template>
  <section class="w-full h-auto md:h-[600px] flex flex-col md:flex-row overflow-hidden">

    <div class="relative w-full md:w-1/2 flex items-center justify-center p-6">
      <div id="carousel-section" class="w-full h-full flex items-center justify-center">
        <Carousel3d
          v-if="slides.length"
          :clickable="true"
          :width="300"
          :height="250"
          :space="250"
          :display="5"
          :border="0"
          :perspective="35"
        >
          <Slide v-for="(slide, i) in slides" :key="i" :index="i">
            <div class="w-full h-full bg-white/50  backdrop-blur-md 
              flex items-center justify-center ring-2 rounded-xl shadow-2xl 
              border relative z-10">
              <h1 class="text-xl  text-center text-white-500 drop-shadow-md">
                {{ slide.name }}
              </h1>
            </div>
          </Slide>
        </Carousel3d>
      </div>
    </div>
    
    <div class="w-full md:w-1/2 flex flex-col items-center justify-center p-8 gap-10">
     <h2
       class="text-center text-4xl md:text-6xl  leading-relaxed
      bg-gradient-to-r from-blue-600 via-indigo-500 to-sky-400
      bg-clip-text text-transparent
      tracking-wide
      px-12 py-6
      bg-white/30 backdrop-blur-xl
      border border-white/30
      rounded-3xl
      shadow-[0_10px_40px_rgba(0,0,0,0.25)]
      px-12 py-6
     "
             >
       Onde entregamos
       <i class="fa-solid fa-people-carry-box"></i>
     </h2>
     <iframe 
       src="./mapa_bahia_lafmed.html"
       class="w-full max-w-[550px] h-[400px] rounded-lg shadow-lg  ring-4 shadow-white/50 drop-shadow-xl"
     ></iframe>
   
   </div>

  </section>
<div class="w-full py-16 flex justify-center">
  
  <ul class="grid grid-cols-1 md:grid-cols-3 gap-10 lg:gap-44">

    <li class="flex justify-center flutuar">
      <div class="w-56 h-56 md:w-64 md:h-64 rounded-full bg-gradient-to-br from-blue-400
       to-blue-600 text-white flex flex-col items-center justify-center
        text-center p-6 transition-all duration-300 ease-in-out hover:-translate-y-3
        hover:scale-105 hover:shadow-[0_20px_50px_rgba(59,130,246,0.4)]">
        <i class="fa-solid fa-chart-column text-5xl mb-3 drop-shadow-md"></i>
        <span class="text-5xl font-extrabold drop-shadow-md">+3K</span>
        <span class="text-lg font-medium mt-1 uppercase tracking-wide">SKU</span>
      </div>
    </li>

    <li class="flex justify-center flutuar atraso-1">
      <div class="w-56 h-56 md:w-64 md:h-64 rounded-full bg-gradient-to-br from-blue-400
       to-blue-600 text-white flex flex-col items-center justify-center text-center
        p-6 transition-all duration-300 ease-in-out hover:-translate-y-3 hover:scale-105
         hover:shadow-[0_20px_50px_rgba(59,130,246,0.4)]">
        <i class="fa-solid fa-diagram-project text-5xl mb-3 drop-shadow-md"></i>
        <span class="text-5xl font-extrabold drop-shadow-md">+30</span>
        <span class="text-base md:text-lg font-medium mt-1 leading-tight">Laboratórios<br>Parceiros</span>
      </div>
    </li>

    <li class="flex justify-center flutuar atraso-2">
      <div class="w-56 h-56 md:w-64 md:h-64 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 text-white flex flex-col items-center justify-center text-center p-6 transition-all duration-300 ease-in-out hover:-translate-y-3 hover:scale-105 hover:shadow-[0_20px_50px_rgba(59,130,246,0.4)]">
        <i class="fa-solid fa-chart-pie text-5xl mb-3 drop-shadow-md"></i>
        <span class="text-5xl font-extrabold drop-shadow-md">+3K</span>
        <span class="text-sm md:text-base  mt-1 leading-tight">Clientes Atendidos<br>Mensalmente</span>
      </div>
    </li>

  </ul>

</div>
</template>

<script setup>
import { Carousel3d, Slide } from 'vue3-carousel-3d';
import 'vue3-carousel-3d/dist/index.css';

const slides = [
  { name: '14 laboratórios parceiros 🧪' },
  { name: 'Mudando vidas ❤️‍🩹' },
  { name: 'Sempre com os melhores preços💲!' },
  { name: 'Entregamos em mais de 7 cidades na Bahia!!' },
  { name: 'Dúvidas? nos contate pelo SAC👤' },
  { name: 'Prontos para entregar onde quiser' }
];
</script>

<style scoped>

/* estlização feita para o carrosel */
:deep(.carousel-3d-slide) {
  background-color: transparent !important; 
  border: none !important;
  box-shadow: none !important; 
  overflow: visible !important;
   width: 100%;
  height: auto;
  object-fit: contain;
  border-radius: 15px;
}
:deep(.carousel-3d-container) {
  overflow: visible !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}


/*animação nde flutuar*/
@keyframes flutuar {
  0%, 100% { 
    transform: translateY(0); 
  }
  50% { 
    transform: translateY(-15px); 
  }
}

.flutuar {
  animation: flutuar 4s ease-in-out infinite;
  will-change: transform; 
}

.atraso-1 {
  animation-delay: 1s;
}

.atraso-2 {
  animation-delay: 2s;
}

</style>

