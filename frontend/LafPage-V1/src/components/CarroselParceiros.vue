<template>
  <div class="w-full h-auto flex items-center justify-center">

    <div class="relative flex flex-col items-center justify-center p-8  gap-10">
      <h1
      class="relative text-center text-6xl md:text-8xl lg:text-9xl
      bg-gradient-to-r from-blue-600 via-indigo-500 to-sky-400
      bg-clip-text text-transparent
      tracking-wide
      px-12 py-6
      bg-white/30 backdrop-blur-xl
      border border-white/30
      rounded-3xl
      shadow-[0_10px_40px_rgba(0,0,0,0.25)]
      ">
         Parceiros 
         nossos
         <i class="fa-solid fa-handshake-angle"></i>
</h1>
      <section
        ref="container"
        class="relative w-full max-w-[1800px] mx-auto h-[30vh] overflow-hidden"
        @mouseenter="pausar"
        @mouseout="iniciar">
        <div
        ref="track"
        class="flex will-change-transform"
        :style="{ transform: `translateX(${posicao}px)`}">
            <img v-for="(image , index) in imagensDuplicadas"
            :key="index"
            :src="image" 
            class="h-[30vh] w-auto flex-shrink-0 object-contain px-6"
            >
        </div>
      </section>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

import img1 from '../assets/airela.png'
import img2 from '../assets/belfar.png'
import img3 from '../assets/brasterapica.png'
import img4 from '../assets/cellera_farma.png'
import img5 from '../assets/cifarma.png'
import img6 from '../assets/geolab.png'
import img7 from '../assets/germed.png'
import img8 from '../assets/globo.png'
import img9 from '../assets/legrand.png'
import img10 from '../assets/medquimica.png'
import img11 from '../assets/multilab.png'
import img12 from '../assets/neo_quimica.png'
import img13 from '../assets/novaquimica.png'
import img14 from '../assets/teuto.png'
import img15 from '../assets/vitamedic.png'
import img16 from '../assets/althaia(1).png'
import img17 from '../assets/pharlab.png'

const imagens = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14,img15,img16,img17]
const imagensDuplicadas = [...imagens, ...imagens]

const posicao = ref(0)
const track = ref(null)

let animacaoFrame = null
const velocidade = 1.2

function animar(){
  posicao.value += velocidade

  const largura = track.value.scrollWidth / 2

  if(posicao.value >= 0){
    posicao.value = -largura
  }

  animacaoFrame = requestAnimationFrame(animar)
}

function iniciar(){
  if(!animacaoFrame){
    animar()
  }
}

function pausar(){
  cancelAnimationFrame(animacaoFrame)
  animacaoFrame = null
}

onMounted(() => {
  iniciar()
})

onUnmounted(() => {
  cancelAnimationFrame(animacaoFrame)
})
</script>