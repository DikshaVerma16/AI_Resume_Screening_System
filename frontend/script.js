async function predictResume(){

    const resume = document.getElementById("resume").value;

    if(resume==""){

        alert("Please paste a resume.");

        return;

    }

    const response = await fetch("http://127.0.0.1:5000/predict",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            resume:resume

        })

    });

    const data = await response.json();

    document.getElementById("result").innerHTML =
    "Predicted Category : <br><br><b>"+data.prediction+"</b>";

}