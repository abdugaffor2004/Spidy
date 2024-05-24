import axios from "axios";

export const getQuestions = async (formData) => {
  const { data } = await axios.post("http://127.0.0.1:8000/upload", formData, 
        {
            headers: {
            "Content-Type": "multipart/form-data",
            },
        }
    );

    return data
};



// export const getQuestions = async (formData) => {
//     const response = await fetch("http://127.0.0.1:8000/upload", {
//       method: "POST",
//       headers: { "Content-Type": "multipart/form-data" },
//       body: JSON.stringify(formData),
//     });

//     return await response.json();
// };