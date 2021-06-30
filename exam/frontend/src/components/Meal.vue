<template>
    <div class="meals"> 
        <p v-if="$root.meal.DDISH_NM !== undefined"></p>
        <div v-on:changed="$root.meal" v-for="meal in $root.meal" v-bind:key="meal.DDISH_NM" v-else>
            <div id="meal">
                <div id = "MMEAL_SC_NM">
                    {{meal.MMEAL_SC_NM}}
                </div>
                <div id = "DDISH_NM">
                    {{meal.DDISH_NM}}
                </div>
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
    mounted() {
        console.log(this.$root.meal.DDISH_NM);
    }
}

</script>

<style lang="scss">
.meals {
    text-align: center;
    display: flex;
}
.meal {
    text-align: center;
    flex:1;
    width: 50px;
    margin-right: 100px;
    font-size: 20pt;
    margin: 0px 5%;
}
#MMEAL_SC_NM {
    border-bottom: thick double #32a1ce;
    font-size: 30pt;
}
#DDISH_NM {
    font-size: 18pt;
}
</style>