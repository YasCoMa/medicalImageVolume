<template>
    <Text class="text-center mb-4" type="title"> Welcome to the Medical Image processing web application </Text>
    <h3>Upload a dicom image (.dcm) to get the corresponding volume (you may drag and drop):</h3>
    <DragDropUpload :multiple="false" />
    
    
</template>

<script lang="ts" setup >

definePageMeta({});

useHead({ title: "Medical Image Application" });

</script>
