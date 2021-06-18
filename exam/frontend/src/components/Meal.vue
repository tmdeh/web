<template>
    <div class="meal"> 
        {{$root.meal.msg}}
    <div class="meal"  v-on:changed="$root.meal" v-for="meal in $root.meal" v-bind:key="meal.DDISH_NM">
            <div id = "MMEAL_SC_NM">
                {{meal.MMEAL_SC_NM}}
            </div>
            <div id = "DDISH_NM">
                {{meal.DDISH_NM}}
            </div>
    </div>
    </div>
</template>

<script>
// import Search from '../components/Search.vue'
export default {
    name:"Meal",
    components: {
    },
    data () {
        return {
        }
    },
}
</script>

