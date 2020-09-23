<template>
  <div id="app">
    <div>
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">Sentiment Analysis</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item>Server Status: {{server_status}}</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col><front :server_status="server_status" :set_server_status="set_server_status"/></b-col>
      </b-row>
    </b-container>    
  </div>
</template>

<script>
import front from './components/front.vue'

export default {
  name: 'App',
  components: {
    front
  },
  data(){
    return{
      server_status: "Busy",
    }
  },
  methods:{
    set_server_status:function(status){
      this.server_status=status
    }
  },
  mounted:function(){
    // Wake server up
    fetch("https://ml-sentiment-analysis-backend.herokuapp.com/wake",{
      method:'get'
    }).then((Response)=>{
      return Response.json()
    }).then((jsonData)=>{
      this.server_status=jsonData['return']
    })
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
