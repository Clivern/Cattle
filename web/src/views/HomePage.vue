<!-- @format -->

<template>
  <div class="home_page">
    <br />
    <div class="columns">
      <div class="column is-full logo">
        <a href="/">
          <img alt="logo" src="../assets/logo.png" width="130" />
        </a>
      </div>
    </div>
    <div class="columns editor">
      <div class="column is-three-fifths">
        <codemirror v-model="code" :options="cmOption" />
        <div class="columns">
          <div class="column is-full editor-footer">
            <b-field grouped>
              <b-field>
                <b-select placeholder="Select Language" disabled>
                  <option value="php">PHP</option>
                  <option value="go">Go</option>
                  <option value="java">Java</option>
                  <option value="python">Python</option>
                  <option value="ruby">Ruby</option>
                  <option value="rust">Rust</option>
                </b-select>
              </b-field>
              <b-field>
                <b-select placeholder="Select Version">
                  <option selected>1.10</option>
                  <option>1.11</option>
                </b-select>
              </b-field>
              <b-field>
                <b-button type="is-warning">Save & Run</b-button>
              </b-field>
            </b-field>
          </div>
        </div>
      </div>
      <div class="column">
        <pre style="min-height: 300px">
Output:
--
Execution time in miliseconds: -
Build time in miliseconds: -
                </pre
        >
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

.CodeMirror {
  font-size: 14px;
}

.editor-footer {
  margin: 12px;
}

.copyright {
  text-align: center;
  margin: 9px;
  font-family: monospace !important;
}

.editor {
  padding: 40px;
}
</style>

<script>
import { codemirror } from "vue-codemirror";
import "codemirror/mode/go/go.js";
import "codemirror/theme/hopscotch.css";

export default {
  name: "home_page",
  components: {
    codemirror,
  },
  data() {
    return {
      // Loader
      loader: {
        isFullPage: true,
        ref: null,
      },

      cmOption: {
        tabSize: 4,
        styleActiveLine: true,
        lineNumbers: true,
        line: true,
        mode: "text/x-go",
        theme: "hopscotch",
      },
      code: `package main

import (
    "fmt"
    "math/rand"
)

func main() {
    fmt.Println("My favorite number is", rand.Intn(10))
}`,
    };
  },

  methods: {
    loading() {
      this.loader.ref = this.$buefy.loading.open({
        container: this.loader.isFullPage ? null : this.$refs.element.$el,
      });
    },
  },

  mounted() {
    /*
        this.$emit("refresh-state");

        this.loading();

        this.$store.dispatch("api_server/fetchApiServerReadiness").then(
            () => {
                this.api_server_status =
                    this.$store.getters["api_server/getApiServerReadiness"].status;

                this.loader.ref.close();
            },
            (err) => {
                this.$buefy.toast.open({
                    message: err,
                    type: "is-danger is-light",
                });

                this.loader.ref.close();
            }
        );
        */
  },
};
</script>
