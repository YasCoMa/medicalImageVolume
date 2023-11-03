<template>
    <Text class="text-center mb-4" type="title"> Welcome to the Medical Image processing web application </Text>
    
    <h3 class="mb-2" >Upload dicom images (.dcm) to get the corresponding volume and pixels above threshold (you may drag and drop):</h3>
    
    <DragDropUpload :multiple="true" />
    
</template>

<script lang="ts" setup >

definePageMeta({});

useHead({ title: "Medical Image Application" });

</script>
