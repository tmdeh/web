<template>
    <div id="school">
        <span @click="submit">-{{school.SCHUL_NM}}- ({{school.ATPT_OFCDC_SC_NM}})</span>
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
            }).catch(() => {
                this.$root.meal = "식단표가 없습니다.";
            });
        },
    }
}
</script>
<style lang="scss">

</style>