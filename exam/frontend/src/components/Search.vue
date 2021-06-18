<template>
    <div id="app">
        <b-form-input id="uinput" v-model="schoolname" @keypress.enter ="submit" placeholder="학교이름"></b-form-input>
        <div class="info">
            <div class="school">
                <School id="school" v-for="school in schools" v-bind:key="school.school_code" v-bind:school="school"></School>
            </div>
            <div class="meal">
                <Meal></Meal>
            </div>
        </div>
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
  margin-bottom: 100px;
}
#uinput {
    margin-left:25%;
    margin-bottom: 100px;
    width: 50%;
    height: 100px;
    border-radius: 5em;
    font-size: 30pt;
}
.info{
    margin: 30px;
    display: flex;
}
.school{
    border-radius: 5px;padding: 0.6em 1em;background: #F1F1F3;
    text-align: center;
    width: 30%;
    position: relative;
    font-size: 25pt;
    flex:1;
}
#school {
    border-radius: 5em; padding: 0.6em 1em; background: #F9F9F9; box-shadow: 1px 2px 10px rgba(0,0,0,0.2);  margin-left: 5px;
    margin-bottom: 15px;
}
.meal{
    width: 60%;
    flex:1;
    border-radius: 5px;padding: 0.6em 1em;background: #F1F1F3;
}

</style>