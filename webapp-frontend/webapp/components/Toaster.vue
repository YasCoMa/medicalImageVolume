<template>
  <Teleport to="body">
      <ul v-if="toastStore.toasts.length" class="toaster__wrapper" >
          <li
            v-for="toast in toastStore.toasts"
            :class="['toaster__inner', toastClassMap[toast.status]]"
            :key="toast.text"
          >
            <a href="javascript:void(0)" @click="toastStore.remove(toast.id);" >
              <div class="flex justify-start" >
                <span class=" px-1 py-1" style="height: 20px" @click="toastStore.remove(toast.id);">
                  <svg class="fill-current h-6 w-6 text-red-500" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                    <title>Close</title>
                    
                    <path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/>
                  </svg>
                </span>

                <strong class="toaster__inner-text-title"> {{ toast.text }} </strong>

              </div>
              <p class="block toaster__inner-text-description"> {{ toast.description }} </p>
            </a>
          </li>
      </ul>
  </Teleport>
</template>

<script setup lang="ts">

const toastClassMap: Record<TToastStatus, string> = {
  warning: "warning",
  error: "error",
  success: "success",
  information: "information"
};

const toastIconMap: Record<TToastStatus, string> = {
  error: "toast-error",
  warning: "toast-warning",
  success: "toast-success",
  information: "toast-information",
};
const toastStore = useToasterStore();

</script>

<style scoped >
.toaster__wrapper {
   position: fixed;
   top: 3%;
   right: 5%;
   z-index: 100;
   display: flex;
   flex-direction: column;
   gap: 1rem;
}
 .toaster__inner {
   --color: black;
   display: flex;
   align-items: center;
   gap: 1rem;
   border-radius: 0.3rem;
   border: 1px solid transparent;
   background-color: white;
   padding: 1rem 1rem;
   border-color: var(--color);
   color: var(--color);
}
 .toaster__inner svg {
   fill: var(--color);
   stroke: var(--color);
}
 .toaster__inner.success {
   --color: green;
}
 .toaster__inner.warning {
   --color: orange;
}
 .toaster__inner.error {
   --color: red;
}
 .toaster__inner.information {
   --color: blue;
}
 .toaster__inner-icon {
   width: 1.8rem;
   aspect-ratio: 1;
}
 .toaster__inner-text-title {
   font-size: 1.2rem;
   font-weight: 600;
}
 .toaster__inner-text-description {
   font-size: 0.8rem;
   font-weight: 300;
}
</style>