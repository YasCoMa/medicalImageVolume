<template>
  <div class="grid grid-cols-1 gap-4 " >
    <label for="dragdrop-file" class="block h-64 relative overflow-hidden rounded">
      <!-- 
      Source: https://danielkelly.io/blog/vue-3-tailwind-file-drag-and-drop-input/
      
      * The input has an "overlayed" class which we define using @apply in the style block below
      * This ensures that no matter where you drag inside of the "drop zone" the default browser behavior for file inputs will kick in and assign that file(s) to the input
      * If we didn't do this the browser would instead just attempt to open the file in the window
      -->
      <input
        id="dragdrop-file"
        type="file"
        class="overlayed"
        :multiple="multiple"
        :value="temp"
        accept=".dcm"
        @change="handleUpload"
      />
      <!-- This is where we do the fancy styling with Tailwind CSS and transform this thing from a normal file input to a nicely styled drag and drop dropzone-->

      <!-- The pointer-events-none class here is very important as it allows our drags and clicks to pass through to the input underneath -->
      <span
        :class="`overlayed bg-${color}-100 border-${color}-200 border-2 text-${color}-800 pointer-events-none flex justify-center items-center`"
      >
        <div class="text-center">
          <!-- Let's use a slot here to make our component a little more flexible (maybe the end developer would live to add an icon in there, etc) -->
          <slot>
            <strong>Upload File(s)</strong>
          </slot>

          <!-- 
          * Print out the file name so the user gets the feedback that the input accepted the file appropriately 
          * This is really the only part that relies on Vue, 
          the actual drag and drop functionality is handled by the default browser behavior for the input. 
          This puts the majority of the functionality on the browser which is great! 
          That means we don't have to mess with it
          -->
          <small v-if="files.length" :class="`text-${color}-600 block`">
            <slot name="file" :files="files" :uploadInfo="uploadInfo">
              {{ uploadInfo }}
            </slot>
          </small>
        </div>
      </span>
    </label>
  
    <div class="flex justify-start " v-if="files.length > 0" >
        <Button 
          @click="calcVolume();"
          class="mx-2"
          style="width: "
          :is-loading="isLoading"
        >
          Calculate Volume
        </Button>
        
        <Button 
          @click="results = []; temp = []; files = [];"
          class="mx-2"
          style="width: "
          :is-loading="isLoading"
          v-if="results.length > 0"
        >
          Clear results
        </Button>
    </div>
    
    <p v-else> <strong>No chosen files yet</strong> </p>
  </div>
  
  <div class="grid grid-cols-4 lg:grid-cols-6 gap-4 mt-4 " v-if="results.length!=0" >
    <Card v-for="d in results" :type="d.error ? 'error' : 'success'" >
        <template #title >
            <span v-if="! d.error" >{{ d.data.name }}</span>
            <span v-else >{{ d.name }}</span>
          </template>

          <template #body >
            <span v-if="! d.error" >
                <p v-if="! d.error" > <strong>Pixels above threshold:</strong> <span> {{ d.data.pixelsAboveCutoff }} </span> </p>
                <p v-if="! d.error" > <strong>Volume:</strong> <span> {{ d.data.volume }}mm³ </span> </p>
            </span>
            
            <span v-else> Incorrect or invalid file </span>
          </template>
    </Card>
  </div>
  
</template>

<style scoped>
.overlayed {
  @apply absolute top-0 left-0 right-0 bottom-0 w-full block;
}
</style>

<script lang="ts" setup>
import { ref, computed, onMounted, onUpdated } from "vue";

const rpmedimg = useMedicalImage();

const files = ref([]);
let volume = ref(0);
let pixelsAbove = ref(0);
let color = "cyan";
let results = ref([]);
let temp = ref([]);
let isLoading = ref(false);

const props = defineProps<{
  multiple: boolean;
}>();

const uploadInfo = computed(() => {
  return files.value.length === 1
    ? files.value[0].name
    : `${files.value.length} files selected: (${ files.value.map( (im) => im.name ).join(', ') })`
})

const handleUpload = (e) => {
  files.value = Array.from(e.target.files).filter( f => f.name.split(".").slice(-1)[0].toLowerCase().includes("dcm") ) || []
  if( Array.from(e.target.files).length > 0 && files.value.length == 0){
    alert('No valid dcm images were uploaded')
  }
}

const calcVolume = () => {
  isLoading.value = true;
  results.value = [];    
  
  if(files.value.length > 0){
    Promise.all( files.value.map( async (im) => {
        let formData = new FormData();
        formData.append('imageFile', im );
        
        let resp = { name: im.name, error: null };
        try{
            resp = await rpmedimg.calculateVolume(formData);
        }
        catch(e){
            console.log(e)
            resp.error = e;
        }
        return resp;
    }) ).then( (res) => {
        results.value = res;
        temp.value = [];
    })
    .finally( () => {
        isLoading.value = false;
    });
  }
  else{
      alert('Upload a valid image')
  }
}

</script>
