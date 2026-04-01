<template>
  <div class="w-full h-10"></div>
  
  <section class="pt-32 w-full px-[10px] pb-32">
    
    <div class="flex flex-col items-center gap-12 md:gap-20">
      
      <h1 class="text-center text-6xl md:text-8xl lg:text-9xl
        bg-gradient-to-r from-white via-indigo-500 to-sky-400
        bg-clip-text text-transparent
        tracking-wide
        px-8 py-10">
        <i class="fa-solid fa-book-open-reader"></i>
        Nosso Catálogo
      </h1>

      <div class="flex items-center justify-center h-24 w-24 animate-bounce border
        border-gray-400 rounded-full text-blue-400 text-5xl">
        <i class="fa-solid fa-cloud-arrow-down"></i>
      </div>

      <div class="w-full flex justify-center">
        <a href="/catalogo_LAFMED.pdf" download="catalogo_LAFMED.pdf"
           class="group relative inline-flex items-center justify-center px-12 py-8 text-white
           transition-all duration-300 bg-white/10 border border-white/20
           rounded-2xl backdrop-blur-xl shadow-xl 
           hover:bg-blue-600 hover:border-blue-400 hover:shadow-blue-500/40 hover:-translate-y-1 active:scale-95">
          <i class="fa-solid fa-file-pdf mr-4 text-5xl text-red-400 group-hover:text-white transition-colors"></i>
          <span class="text-xl font-semibold">Baixar Catálogo Completo</span>
        </a>
      </div>

    </div>
  </section>
</template>