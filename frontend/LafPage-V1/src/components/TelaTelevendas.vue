<template>
<section class="w-full flex flex-col items-center px-6 py-12 md:p-24 gap-12 md:gap-20">
   <!-- Com o flex e flex-col ou flex-contaier tudo que elstá dentro da  div
    vira um elemento que pose ser manipulado livremente e o p de padding indica seu espaçamento
    dentro do elemento com o px e py sendo seus eixo de cima e vertical-->
 <div class="max-w-6xl mx-auto text-center py-20 px-6 bg-black/20 backdrop-blur-lg rounded-[4rem] border-t border-white/10 shadow-2xl group">
  <h2 class="text-white text-sm  uppercase tracking-[0.3em] mb-8 opacity-70">Ofertas de hoje</h2>
  
  <h1 class="text-5xl md:text-8xl  text-white leading-tight">
    <!-- o mb: é utilizado para se referir especificamente aos desktop e o lg: ao tablets 
     para que ao se use um desses dispositivos não haja quebra de layout-->
    Gostou das <br/>
    <span class="inline-flex items-center gap-2 md:gap-4">
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">
        nossas promos
      </span>
      <!-- Ícones utilizados do font awesome e que foi colocado no index.html para permitir seus usos -->
      <i class="fa-solid fa-tags text-blue-500 text-4xl md:text-7xl rotate-12
       group-hover:rotate-0 transition-transform duration-300"></i>
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">?</span>
    </span>
  </h1>
   <!-- o m se refere a margin do elemento e igual ao p(padding) quase todas as suas custmizações sãoparecidas 
    podendo assim como padding deixar como automático do site-->
  <p class="mt-12 text-blue-100/60 text-lg md:text-xl max-w-xl mx-auto">
    Confira os itens selecionados com descontos de até 50% para sua cidade.
  </p>
</div>




  <div class="max-w-7xl w-full px-4 md:px-12 py-10 md:py-20 rounded-3xl
   bg-white/5 backdrop-blur-md border border-white/10 shadow-2xl">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-16 items-center">
      <!-- o grid ele pega uma tela e a divide a sua escolha , nesse caso como fiz 
       grid gti-cols-1 divie a tela  em uma cla e mias a frente em duas coluna iguais -->
      
      <p class="text-xl md:text-2xl lg:text-3xl text-left text-gray-100 leading-relaxed 
       italic">
        Aproveite nossas <span class="font-bold text-blue-400">ofertas exclusivas<i class="fa-solid fa-capsules"></i></span> por tempo limitado. 
        Trabalhamos com produtos de qualidade e condições imperdíveis.
        <br><br>
        Entre em contato com a nossa equipe de <span class="font-bold text-blue-400">televendas</span>
        e garanta seu lote com a melhor entrega do mercado.
        <i class="fa-solid fa-route text-blue-400 ml-2"></i>
      </p>

      <div class="flex justify-center">
        <img class="rounded-2xl shadow-2xl border-2 border-white/20 object-cover w-full
         max-w-sm md:max-w-md transition-transform duration-500 hover:scale-105" 
        src="../assets/televendas.jpg"
        alt="televendas">
      </div>
    </div>
  </div>

 <div class="w-full flex justify-center mt-8 px-4">
    <a href="https://wa.me/558005910367" target="_blank"
       class="group inline-flex items-center gap-8 p-2 pr-10
              bg-white/5 backdrop-blur-xl border border-white/10
              rounded-[2.5rem] transition-all duration-500
              hover:bg-white/10 hover:shadow-[0_0_50px_rgba(59,130,246,0.3)]
              no-underline">
        <div class="flex flex-col">
            <span class="text-white text-xl md:text-4xl  leading-none">CLIQUE PARA COMPRAR</span>
            <span class="text-blue-400 group-hover:text-green-400  
            text-center font-medium mt-2 transition-colors italic">Encomende online agora →</span>
        </div>
        <div class="p-6 md:p-8 shadow-lg group-hover:from-green-500 group-hover:to-emerald-600
         transition-all duration-500 group-hover:rotate-12">
          <i class="fa-brands fa-whatsapp text-white group-hover:text-green-500 text-4xl md:text-6xl 
          animate-[pulse_2s_infinite] transition-colors duration-500"></i>
         </div>
    </a>
</div>
</section>
</template>
