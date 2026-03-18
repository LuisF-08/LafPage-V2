<template>
  <div class="w-full flex justify-center">
    <div
      ref="container"
      class="relative w-full max-w-9xl h-[70vh] overflow-hidden"
      @mouseenter="pausar"
      @mouseout="iniciar"
    >
      <div
        ref="track"
        class="flex will-change-transform"
        :style="{ transform: `translateX(${posicao}px)` }"
      >
        <img
          v-for="(image, index) in imagensDuplicadas"
          :key="index"
          :src="image"
          class="h-[70vh] w-auto flex-shrink-0 object-cover ring-4 ring-blue-700"
        />
      </div>
    </div>
  </div>
</template>
<script setup>
import img4 from '../assets/equipe-do-armazem.avif'
import img1 from '../assets/capara-homem-lafmed.png'
import img3 from '../assets/vendedor.avif'
import img2 from '../assets/Ofertas-da-Semana-Medicamentos-Lafmed.png'

import { ref, onMounted, onUnmounted } from 'vue'

const imagens = [img1, img2, img3, img4]
const imagensDuplicadas = [...imagens, ...imagens]

const container = ref(null)
const track = ref(null)

const posicao = ref(0)

let animationFrame = null
const velocidade = 1.2

function animar() {

  posicao.value -= velocidade

  const larguraTotal = track.value.scrollWidth / 2

  if (Math.abs(posicao.value) >= larguraTotal) {
    posicao.value = 0
  }

  animationFrame = requestAnimationFrame(animar)
}

function iniciar() {
  if (!animationFrame) animar()
}

function pausar() {
  cancelAnimationFrame(animationFrame)
  animationFrame = null
}

onMounted(() => {
  iniciar()
})

onUnmounted(() => {
  cancelAnimationFrame(animationFrame)
})
</script>