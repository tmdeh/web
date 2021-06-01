<template>
    <div>
        {{ message }}
        <button v-on:click="buttonClicked" v-bind:title="message">클릭!</button>
        <br>
        <input type="test" v-bind:value="message" @change="onChange" @keypress="onKeypress">
    </div>
</template>
<script>
//v-bind = :
//v-on = @
//
export default {
    name: 'Example',
    data () {
        return {
            message: '안녕하세요'
        }
    },
    methods: {
        buttonClicked () {
            this.message = '반갑습니다.'
        },
        onChange(event){
            console.log('onchange', event.target.value);
            this.message = event.target.value;
        },
        onKeypress(event){
            console.log(event.which, event.key);
            if(event.which == 13){
                //로그인
            }
        },
    },
    mounted(){
        console.log("마운트")
    }
}
</script>