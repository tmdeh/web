<template>
  <div id="app">
    <b-form-input v-model="schoolname" @keyup.enter ="submit" placeholder="학교이름"></b-form-input>
    <router-view/>
  </div>
</template>

<script>

  export default {
    data() {
      return {
        schoolname: ''
      }
    },
    methods:{
      submit:function(){
        this.schoolname = "";
    }
  }
}
</script>

<style lang="scss">
#app {
  margin-top: 60px;
  margin-bottom: 60px;

}
</style>