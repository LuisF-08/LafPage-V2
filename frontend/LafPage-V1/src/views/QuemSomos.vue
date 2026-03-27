<template >
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
   <a href="https://wa.me/558005910367"
   target="_blank"
   class="fixed bottom-8 right-8 bg-green-500 text-white
    w-20 h-20 flex items-center justify-center rounded-full
   shadow-[0_10px_25px_rgba(34,197,94,0.4)] hover:bg-green-600 hover:scale-110
    transition-all duration-300 group z-[9999]"
   title="Fale com a gente!">
    <i class="fa-brands fa-whatsapp text-5xl"></i>
    <span class="absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75 animate-ping -z-50"></span>
    </a>
  </div>
  <div>
   <h1>LISTA SAC RESPOSTAS</h1>
  
   <table>
    <thead>
      <tr>
        <th>NOME</th>
        <th>EMAIL</th>
        <th>PEDIDO</th>
        <th>PROBLEMA</th>
        <th>SITUAÇÃO</th>
        <th>RESPOSTA</th>
        <TH>STATUS</TH>
      </tr>
    </thead>

    <tbody>
      <tr v-for="item in sacList" :key="item.pedido">
        <td>{{ item.nome }}</td>
        <td>{{ item.email }}</td>
        <td>{{ item.pedido }}</td>
        <td>{{ item.problema }}</td>
        <td>{{ item.situacao }}</td>
        <td>{{ item.resposta }}</td>
        <td>{{ item.status }}</td>
      </tr>
    </tbody>

   </table>
  
  
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      sacList: []
    };
  },

  mounted() {
    this.buscarDados();
  },

  methods: {
    async buscarDados() {
      try {
        const resp = await axios.get("http://localhost:8000/sac");
        this.sacList = resp.data;
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    }
  }
};
</script>