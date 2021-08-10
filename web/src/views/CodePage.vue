<!-- @format -->

<template>
  <div class="code_page">
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
                <b-select
                  v-model="form.lang"
                  placeholder="Select Language"
                  disabled="disabled"
                >
                  <option value="php">PHP</option>
                  <option value="go">Go</option>
                  <option value="java">Java</option>
                  <option value="python">Python</option>
                  <option value="ruby">Ruby</option>
                  <option value="rust">Rust</option>
                  <option value="c">C</option>
                  <option value="cplus">C++</option>
                </b-select>
              </b-field>

              <!-- If PHP Selected -->
              <template v-if="form.lang == 'php'">
                <b-field>
                  <b-select
                    v-model="form.version"
                    placeholder="Select Version"
                    disabled="disabled"
                  >
                    <option value="7.0">7.0</option>
                    <option value="7.1">7.1</option>
                    <option value="7.2">7.2</option>
                    <option value="7.3">7.3</option>
                    <option value="7.4">7.4</option>
                    <option value="8.0">8.0</option>
                    <option value="8.1">8.1</option>
                  </b-select>
                </b-field>
              </template>

              <!-- If Go Selected -->
              <template v-if="form.lang == 'go'">
                <b-field>
                  <b-select
                    v-model="form.version"
                    placeholder="Select Version"
                    disabled="disabled"
                  >
                    <option value="1.8">1.8</option>
                    <option value="1.9">1.9</option>
                    <option value="1.10">1.10</option>
                    <option value="1.11">1.11</option>
                    <option value="1.12">1.12</option>
                    <option value="1.13">1.13</option>
                    <option value="1.14">1.14</option>
                    <option value="1.15">1.15</option>
                    <option value="1.16">1.16</option>
                    <option value="1.17">1.17</option>
                  </b-select>
                </b-field>
              </template>

              <!-- If Java Selected -->
              <template v-if="form.lang == 'java'">
                <b-field>
                  <b-select
                    v-model="form.version"
                    placeholder="Select Version"
                    disabled="disabled"
                  >
                    <option value="10.0">10.0</option>
                    <option value="11.0">11.0</option>
                    <option value="12.0">12.0</option>
                    <option value="13.0">13.0</option>
                    <option value="14.0">14.0</option>
                    <option value="15.0">15.0</option>
                    <option value="16.0">16.0</option>
                    <option value="17.0">17.0</option>
                  </b-select>
                </b-field>
              </template>

              <!-- If Python Selected -->
              <template v-if="form.lang == 'python'">
                <b-field>
                  <b-select
                    v-model="form.version"
                    placeholder="Select Version"
                    disabled="disabled"
                  >
                    <option value="2.7">2.7</option>
                    <option value="3">3</option>
                    <option value="3.6">3.6</option>
                    <option value="3.7">3.7</option>
                    <option value="3.8">3.8</option>
                    <option value="3.9">3.9</option>
                    <option value="3.10">3.10</option>
                  </b-select>
                </b-field>
              </template>

              <!-- If Ruby Selected -->
              <template v-if="form.lang == 'ruby'">
                <b-field>
                  <b-select
                    v-model="form.version"
                    placeholder="Select Version"
                    disabled="disabled"
                  >
                    <option value="2.6">2.6</option>
                    <option value="2.6.1">2.6.1</option>
                    <option value="2.6.2">2.6.2</option>
                    <option value="2.6.3">2.6.3</option>
                    <option value="2.6.4">2.6.4</option>
                    <option value="2.6.5">2.6.5</option>
                    <option value="2.6.6">2.6.6</option>
                    <option value="2.6.7">2.6.7</option>
                    <option value="2.6.8">2.6.8</option>
                    <option value="2.6.9">2.6.9</option>
                    <option value="2.7.0">2.7.0</option>
                    <option value="2.7.1">2.7.1</option>
                    <option value="2.7.3">2.7.3</option>
                    <option value="2.7.4">2.7.4</option>
                    <option value="2.7.5">2.7.5</option>
                    <option value="3.0.0">3.0.0</option>
                  </b-select>
                </b-field>
              </template>

              <!-- If Rust Selected -->
              <template v-if="form.lang == 'rust'">
                <b-field>
                  <b-select
                    v-model="form.version"
                    placeholder="Select Version"
                    disabled="disabled"
                  >
                    <option value="1.54.0">1.54.0</option>
                    <option value="1.55.0">1.55.0</option>
                    <option value="1.56.0">1.56.0</option>
                    <option value="1.57.0">1.57.0</option>
                    <option value="1.58.0">1.58.0</option>
                    <option value="1.58.1">1.58.1</option>
                  </b-select>
                </b-field>
              </template>

              <!-- If C Selected -->
              <template v-if="form.lang == 'c'">
                <b-field>
                  <b-select
                    v-model="form.version"
                    placeholder="Select Version"
                    disabled="disabled"
                  >
                    <option value="9.4.0">GCC 9.4.0</option>
                  </b-select>
                </b-field>
              </template>

              <!-- If C++ Selected -->
              <template v-if="form.lang == 'cplus'">
                <b-field>
                  <b-select
                    v-model="form.version"
                    placeholder="Select Version"
                    disabled="disabled"
                  >
                    <option value="9.4.0">GCC 9.4.0</option>
                  </b-select>
                </b-field>
              </template>

              <b-field>
                <b-button type="is-warning" @click="runCode()">Run</b-button>
              </b-field>
            </b-field>
          </div>
        </div>
      </div>
      <div class="column">
        <pre style="min-height: 300px">{{ output }}</pre>
      </div>
    </div>
    <br /><br />
    <div class="columns">
      <div class="column is-full copyright">
        Powered by
        <a
          href="https://github.com/Clivern/Cattle"
          target="_blank"
          rel="noopener"
        >
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
import "codemirror/mode/rust/rust.js";
import "codemirror/mode/clike/clike.js";
import "codemirror/mode/python/python.js";
import "codemirror/mode/ruby/ruby.js";
import "codemirror/mode/php/php.js";
import "codemirror/theme/hopscotch.css";

export default {
  name: "code_page",
  components: {
    codemirror,
  },
  data() {
    return {
      form: {
        lang: "python",
        version: "",
      },

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
        readOnly: "nocursor",
      },
      code: "",
      id: "",
      output: "",
    };
  },

  methods: {
    loading() {
      this.loader.ref = this.$buefy.loading.open({
        container: this.loader.isFullPage ? null : this.$refs.element.$el,
      });
    },

    runCode() {
      this.output = "Sit tight while we run your code ...";
      this.loading();

      this.$store
        .dispatch("api/post", {
          uri: "/api/v1/code/" + this.id + "/run",
        })
        .then(
          (response) => {
            var timer = setInterval(() => {
              this.$store
                .dispatch("api/get", {
                  uri: "/api/v1/task/" + response.data.id,
                })
                .then(
                  (response) => {
                    let status = response.data.status;

                    if (status == "SUCCEEDED") {
                      this.output = response.data.result.output;
                      this.output += "\n\n----\n";

                      if (response.data.result.build_time != null) {
                        this.output +=
                          "Build Time: " +
                          response.data.result.build_time +
                          " Milliseconds\n";
                      }

                      if (response.data.result.execution_time != null) {
                        this.output +=
                          "Execution Time: " +
                          response.data.result.execution_time +
                          " Milliseconds\n";
                      }

                      this.output += "\n";

                      this.loader.ref.close();
                      clearInterval(timer);
                    }

                    if (status == "FAILED") {
                      this.output = response.data.result.output;
                      this.output += "\n";

                      this.loader.ref.close();
                      clearInterval(timer);
                    }
                  },
                  (err) => {
                    // TODO: Fix this
                    this.output = err.response.data.errorMessage;
                    this.loader.ref.close();
                  }
                );
            }, 2000);
          },
          (err) => {
            // TODO: Fix this
            this.output = err.response.data.errorMessage;
            this.loader.ref.close();
          }
        );
    },

    initCodeItem() {
      this.loading();

      this.$store
        .dispatch("api/get", {
          uri: "/api/v1/code/" + this.$route.params.id,
        })
        .then(
          (response) => {
            this.id = response.data.uuid;
            this.form.lang = response.data.language;
            this.form.version = response.data.version;
            this.code = response.data.content;

            if (this.form.lang == "java") {
              this.cmOption.mode = "text/x-java";
            }

            if (this.form.lang == "php") {
              this.cmOption.mode = "text/x-php";
            }

            if (this.form.lang == "python") {
              this.cmOption.mode = "text/x-python";
            }

            if (this.form.lang == "ruby") {
              this.cmOption.mode = "text/x-ruby";
            }

            if (this.form.lang == "go") {
              this.cmOption.mode = "text/x-go";
            }

            if (this.form.lang == "rust") {
              this.cmOption.mode = "text/x-rustsrc";
            }

            if (this.form.lang == "c") {
              this.cmOption.mode = "text/x-java";
            }

            if (this.form.lang == "cplus") {
              this.cmOption.mode = "text/x-java";
            }

            this.$store
              .dispatch("api/post", {
                uri: "/api/v1/code/" + response.data.uuid + "/run",
              })
              .then(
                (response) => {
                  var timer = setInterval(() => {
                    this.$store
                      .dispatch("api/get", {
                        uri: "/api/v1/task/" + response.data.id,
                      })
                      .then(
                        (response) => {
                          let status = response.data.status;

                          if (status == "SUCCEEDED") {
                            this.output = response.data.result.output;
                            this.output += "\n\n----\n";

                            if (response.data.result.build_time != null) {
                              this.output +=
                                "Build Time: " +
                                response.data.result.build_time +
                                " Milliseconds\n";
                            }

                            if (response.data.result.execution_time != null) {
                              this.output +=
                                "Execution Time: " +
                                response.data.result.execution_time +
                                " Milliseconds\n";
                            }

                            this.output += "\n";

                            this.loader.ref.close();
                            clearInterval(timer);
                          }

                          if (status == "FAILED") {
                            this.output = response.data.result.output;
                            this.output += "\n";

                            this.loader.ref.close();
                            clearInterval(timer);
                          }
                        },
                        (err) => {
                          // TODO: Fix this
                          this.output = err.response.data.errorMessage;
                          this.loader.ref.close();
                        }
                      );
                  }, 2000);
                },
                (err) => {
                  // TODO: Fix this
                  this.output = err.response.data.errorMessage;
                  this.loader.ref.close();
                }
              );
          },
          () => {
            this.loader.ref.close();
            this.$router.push({ name: "NotFoundPage" });
          }
        );
    },
  },

  mounted() {
    this.initCodeItem();
  },
};
</script>
