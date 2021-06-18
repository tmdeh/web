<template>
    <div>
        <!--<router-link to="meal/" v-bind="school" v-on:click="getMeal"> {{school.school_name}} ({{school.EOName}})</router-link>
         <a href="/meal" v-bind:school="school">{{school.school_name}} ({{school.EOName}})</a> -->
        <span @click="submit">{{school.SCHUL_NM}} ({{school.ATPT_OFCDC_SC_NM}})</span>
        
        <!-- <div class="meals">
            <Meal v-if="meal !== []" v-bind:meal="meal"></Meal>
        </div> -->
    </div>
</template>

<script>
export default {
    name:"School",
    props: ['school'],
    data () {
        return {
            meal: []
        }
    },
    methods: {
        submit:function(){
            this.$axios.get('http://web.dgsw.kr/api/meals', {
                params: {
                    sc_code: this.school.ATPT_OFCDC_SC_CODE, // 시도교육청코드
                    schul_code: this.school.SD_SCHUL_CODE, // 학교코드
                }
            }).then(resp => {
                this.$root.meal = resp.data.meals;
                //MMEAL_SC_NM 조식 중식 석식
                //DDISH_NM 메뉴이름
            }).catch(() => {
                this.$root.meal = "식단표가 없습니다.";
            });
        },
    }
}
</script>
