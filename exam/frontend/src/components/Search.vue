<template>
    <div id="app">
        <b-form-input id="uinput" v-model="schoolname" @keypress.enter ="submit" placeholder="학교이름"></b-form-input>
        <School v-for="school in schools" v-bind:key="school.school_code" v-bind:school="school"></School>
        <Meal></Meal>
    </div>
</template>
<script>
import School from './School.vue';
import Meal from './Meal.vue';
export default {
  components: { 
      Meal,
      School 
      },
    name: "Search",
    data() {
        return {
            schoolname: '',
            schools: []
        }
    },
    methods : {
        submit:function() {
            this.$axios.get('http://web.dgsw.kr/api/schools', {params: {query: this.schoolname}}).then(resp => {
                /*
ATPT_OFCDC_SC_CODE: "B10"
ATPT_OFCDC_SC_NM: "서울특별시교육청"
HMPG_ADRES: "http://www.daemyeong.ms.kr"
SCHUL_KND_SC_NM: "중학교"
SCHUL_NM: "대명중학교"
SD_SCHUL_CODE: "7091424"
*/
                this.schools = resp.data.schools
                /*
                this.schools.splice(0)
                for (let school of resp.data.schools) {
                    
                }*/

            })
        },
        // submit:function(){
        //     let url = "/api/" + this.schoolname
        //     this.$axios.get(url).then((res) => {
        //         this.schools = res.data;
        //     });
        // }
    }
}
</script>

<style lang="scss">
#app {
  margin-top: 60px;
  margin-bottom: 60px;
}
#uinput {
    margin-left:25%;
    width: 50%;
}

</style>