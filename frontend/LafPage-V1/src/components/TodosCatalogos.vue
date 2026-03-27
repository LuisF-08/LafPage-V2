<template>
  <div class="w-full h-40"></div>

   <!-- o w full já deixa tudo em tamanho máximo e o h-40 deixa com um tamanho já predefinido -->

  <section class="w-full px-4 py-12 md:py-24 flex flex-col items-center gap-24">

    <!-- O max-w-[] ele deixa especifcicado o tamanho de cada coisa -->
     <!-- toda essa página foi feita inteiramente paa guardar os catálogos que da empresa
      e são fatiados em até 5 partes onde o fornecedor desse seviço permtiu segundo seus termos -->

    <div class="w-full max-w-[1100px] bg-white/5 backdrop-blur-xl
     border border-white/10 shadow-2xl p-6 md:p-10 rounded-[40px]">
      <div class="flex flex-col items-center mb-8 border-b border-white/10 pb-6 gap-4">
        <div class="flex flex-wrap justify-center items-center gap-6">
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center justify-center">
            <img class="max-h-full object-contain" src="../assets/teuto.png" alt="Teuto">
          </div>
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center justify-center">
            <img class="max-h-full object-contain" src="../assets/neo_quimica.png" alt="Neo Química">
          </div>
        </div>
        <span class="text-white/50 text-sm tracking-widest uppercase">Páginas 0 - 44</span>
      </div>


      <div class="w-full h-[450px] md:h-[600px] rounded-2xl overflow-hidden border border-white/10 bg-black/20">
        <iframe src="https://heyzine.com/flip-book/5b13a96f47.html"
         class="w-full h-full" frameborder="0" allowfullscreen loading="lazy"></iframe>
      </div>
    </div>

    <div class="w-full max-w-[1100px] bg-white/5 backdrop-blur-xl border
     border-white/10 shadow-2xl p-6 md:p-10 rounded-[40px]">
      <div class="flex flex-col items-center mb-8 border-b border-white/10 pb-6 gap-4">
        <div class="flex flex-wrap justify-center items-center gap-6">
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/legrand.png" alt="Legrand"></div>
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/germed.png" alt="Germed"></div>
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center 
          justify-center"><img class="max-h-full object-contain" src="../assets/airela.png" alt="Airela"></div>
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/vitamedic.png" alt="Vitamedic"></div>
        </div>
        <span class="text-white/50 text-sm tracking-widest uppercase">Páginas 44 - 84</span>
      </div>
      <div class="w-full h-[450px] md:h-[600px] rounded-2xl overflow-hidden border border-white/10 bg-black/20">
        <!-- Iframe é utlizado para puxar coisas de outros sites para o seus html, , puxei do site 
         dos flibooks para o nosso para evitar uma ospedagem de um arquivo pequeno-->
        <iframe src="https://heyzine.com/flip-book/9a1e903af7.html" class="w-full h-full" frameborder="0" allowfullscreen loading="lazy"></iframe>
      </div>
    </div>

    <div class="w-full max-w-[1100px] bg-white/5 backdrop-blur-xl border
     border-white/10 shadow-2xl p-6 md:p-10 rounded-[40px]">
      <div class="flex flex-col items-center mb-8 border-b border-white/10 pb-6 gap-4">
        <div class="flex flex-wrap justify-center items-center gap-6">
          <!-- o rounded literalmente arredondas coisas de acordo com seu estilo e o gap define espaço entre
           os elementos dentro de uma mesmam div sem precisar colocar em cada item individualmente-->
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/globo.png" alt="Globo"></div>
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/althaia.png" alt="Althaia"></div>
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/belfar.png" alt="Belfar"></div>
        </div>
        <span class="text-white/50 text-sm tracking-widest uppercase">Páginas 84 - 99</span>
      </div>
      <div class="w-full h-[450px] md:h-[600px] rounded-2xl
       overflow-hidden border border-white/10 bg-black/20">
        <iframe src="https://heyzine.com/flip-book/6acb1e1764.html"
         class="w-full h-full" frameborder="0" allowfullscreen loading="lazy"></iframe>
      </div>
    </div>

    <div class="w-full max-w-[1100px] bg-white/5 backdrop-blur-xl border
     border-white/10 shadow-2xl p-6 md:p-10 rounded-[40px]">
      <div class="flex flex-col items-center mb-8 border-b border-white/10 pb-6 gap-4">
        <div class="flex flex-wrap justify-center items-center gap-6">
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/pharlab.png" alt="Pharlab"></div>
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/multilab.png" alt="Multilab"></div>
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/novaquimica.png" alt="Nova Química"></div>
        </div>
        <span class="text-white/50 text-sm tracking-widest uppercase">Páginas 99 - 120</span>
      </div>
      <div class="w-full h-[450px] md:h-[600px] rounded-2xl overflow-hidden border border-white/10 bg-black/20">
        <iframe src="https://heyzine.com/flip-book/98ca1eba1f.html"
         class="w-full h-full" frameborder="0" allowfullscreen loading="lazy"></iframe>
      </div>
    </div>

    <div class="w-full max-w-[1100px] bg-white/5 backdrop-blur-xl
     border border-white/10 shadow-2xl p-6 md:p-10 rounded-[40px]">
      <div class="flex flex-col items-center mb-8 border-b border-white/10 pb-6 gap-4">
        <div class="flex flex-wrap justify-center items-center gap-6">
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/brasterapica.png" alt="Brasterápica"></div>
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/geolab.png" alt="Geolab"></div>
          <div class="bg-white p-2 rounded-xl w-24 h-16 flex items-center
           justify-center"><img class="max-h-full object-contain" src="../assets/medquimica.png" alt="Medquímica"></div>
        </div>
        <span class="text-white/50 text-sm tracking-widest uppercase">Páginas 120 - 144</span>
      </div>
      <div class="w-full h-[450px] md:h-[600px] rounded-2xl overflow-hidden border
       border-white/10 bg-black/20">
        <iframe src="https://heyzine.com/flip-book/b9618eb61f.html"
         class="w-full h-full" frameborder="0" allowfullscreen loading="lazy"></iframe>
      </div>
    </div>


    <div class="w-full max-w-[800px] mx-auto mt-20 pb-12 px-6 text-center">
     <p class="text-white/30 text-[10px] uppercase tracking-[2px] leading-relaxed">
      Tecnologia de exibição fornecida por 
      <a href="https://heyzine.com" target="_blank" class="hover:text-indigo-400
      transition-colors underline decoration-white/10">Heyzine Flipbooks</a>. 
      Os catálogos são de responsabilidade da <span class="font-bold text-blue-600">LAFMED</span> e marcas parceiras.
      </p>
      <!-- o :hover e trasition são as funções que facilitão as  manipulações de items 
       para deixa-los estilizados com o tailwind assim como as animações padrões da biblioteca-->
   </div>
   <!-- TOdos os direitos reservados ao Heyzine FlipBooks que permite essa alocação
     de catálogos via servidor deles
    e a LAFMED por usar os icones dos seus parceiros-->
  </section>
</template>