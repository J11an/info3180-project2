<template>

        <div class="row  align-items-center">

            <div class="col-lg-7 p-3 p-lg-5 pt-lg-3">
                <h1 class="display-4 fw-bold lh-1">Buy and Sell Cars Online</h1>
                <p class="lead">United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell cars online.
                        Find a Great Price on a Vehicle You Want.</p>
                <div class="d-grid gap-2 d-md-flex justify-content-md-start mb-4 mb-lg-3">
                    <button type = "button" @click="Register" class = "btn btn-primary rbtn shadow">Register</button>
                    <button type = "button" @click="Login" class = "btn btn-success lbtn shadow">Login</button>
                </div>
            </div>

            <div class="col-lg-4 shadow-lg">
                <img src="@/assets/HomePage.png" class = 'homeimg'>
            </div>

        </div>
    
</template>

<script>

import homeimg from '../assets/HomePage.png'
export default{

    data(){

        return {image : homeimg}
    },

methods:
{
    Register(){
        this.$router.push('/register');
    },

    Login(){
        this.$router.push('/login');
    }
}
}
</script>



<style scoped>

* {    
    margin:0px;
    padding:0px;
}
body::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
body {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
  overflow: hidden;
}

.rbtn{

    padding:10px 45px 10px 45px;
    border-radius: 10px;
    

}

.lbtn{

    padding:10px 53.8px 10px 53.8px;
    border-radius: 10px;

}

</style>