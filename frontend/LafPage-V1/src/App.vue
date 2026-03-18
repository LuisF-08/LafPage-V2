<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div id="app" class="min-h-screen flex flex-col overflow-x-hidden">

    <Header/>

    <main class="flex-1 w-full pt-32">
      <router-view />
    </main>

    <Footer/>

  </div>
</template>

<style>
body {
  margin: 0;
  padding: 0;
}

</style>