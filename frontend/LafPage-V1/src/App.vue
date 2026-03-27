<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

//Página de inicialização  de todo o site vai por ele que irá ser 
// póssivel usar o vue-routes para ir para outras aba 
</script>

<template>
  <div id="app" class="min-h-screen flex flex-col overflow-x-hidden">
    <!-- Montei o header separado para não causar problemas na refatoração-->
    <Header/>
    <main class="flex-1 w-full pt-32">
      <!-- Função do vue utilizado para criar rotas de forma dinâmica e simples-->
      <router-view />
    </main>
    <Footer/>
    <!-- Montei o footer separado peloe mesmos motivos do header -->
  </div>
</template>
<style>
/* estilo padrão de site para não dificlutar
as próximas mudanças feitas em cada página */
body {
  margin: 0;
  padding: 0;
}

</style>