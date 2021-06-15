<template>
    <div>
        {{schools}}
    </div>
</template>

<script>
// schools =[]
// this.$axios.get('/').then((res) => { // resp.data : 응답 본문 데이터

// })
export default {
    data () {
    return {
        schools:[
            "고등학교1", "고등학교2", "고등학교3"
        ]}
    }  
}
</script>