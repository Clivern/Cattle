<!-- @format -->

<template>
  <div class="not_found_page">
    <br />
    <div class="columns">
      <div class="column is-full logo">
        <a href="/">
          <img alt="logo" src="../assets/logo.png" width="130" />
        </a>
      </div>
    </div>
    <div class="columns">
      <div class="column is-full" style="text-align: center">
        <img alt="art" src="../assets/01.png" width="500" />
        <br /><br />
        <div style="font-family: monospace">
          Oops! It looks like we can't find what you’re looking for.
        </div>
      </div>
    </div>
    <br /><br />
    <div class="columns">
      <div class="column is-full copyright">
        Powered by
        <span class="icon has-text-danger"><i class="fas fa-rocket"></i></span>
        <a href="https://clivern.com/" target="_blank" rel="noopener">
          Clivern</a
        ><br />
      </div>
    </div>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #42b983;
}
</style>

<style>
.logo {
  text-align: center;
  margin: 10px;
}

.copyright {
  text-align: center;
  margin: 9px;
  font-family: monospace !important;
}
</style>
