<template>
  <div >
    <a 
      :href="link" 
      @click="_onClick()"
      :class="`block max-w-sm p-6 border border-gray-200 rounded-lg ${bg} ${text500} `"
    >
      <h5 
        class="mb-2 text-2xl font-bold tracking-tight  "
      >
        <slot name="title" />
      </h5>

      <p 
        class="font-normal  "
      >
        <slot name="body" />
      </p>

    </a>

  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, onUpdated, } from "vue";

const props = defineProps<{
  type: "info" | "error" | "warning" | "success";
  onClick?: () => void;
  link?: string;
}>();

const bg = ref("bg-gray-300");
const text500 = ref("text-[#00000]");

function setColors(){
  if(props.type === "error"){
    bg.value = "bg-red-500";
    text500.value = "text-white";
  }else if(props.type === "warning"){
    bg.value = "bg-orange-500";
    text500.value = "text-[#ffffff]";
  }else if(props.type === "success"){
    bg.value = "bg-green-500";
    //text500.value = "text-orange-500";
  }
}

function _onClick(){
  if(props?.onClick){
    props?.onClick();
  }
}

onMounted(() => {
  setColors();
});

</script>