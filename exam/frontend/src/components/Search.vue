<template>
    <div id="app">
        <b-form-input v-model="schoolname" @keyup.enter ="submit" placeholder="학교이름"></b-form-input>
    </div>
</template>
<script>
const url = "/" + this.schoolname;
export default {
    name: "Search",
    data() {
        return {
            schoolname: ''
        }
    },
    methods : {
        submit:function(){
            this.$axios.get(url).then((res) => {
                console.log(res);
            });
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