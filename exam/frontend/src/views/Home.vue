<template>
  <div class="home">
    <School></School>
  </div>
</template>

<script>
// @ is an alias to /src
import School from '../components/School.vue'

export default {
  name: 'Home',
  components: {
   School
  },
  data() {
    return {
    }
  }
}
</script>
