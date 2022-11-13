
function setItem() {console.log("data stored");}

function gotdata({data}) {
    $("#news-prediction").text(data['news_pred']);
    $("#news-polarity").text(data['polarity_pred']);
    $("#news-subjectivity").text(data['subjectivity_pred']);
}

function onError(error) {console.log(error)}

browser.tabs.query({currentWindow: true, active: true}).then(
        (tabs_info) => {
            let uri = tabs_info[0].url;

            browser.storage.local.get("data").then(
                ({data}) => {
                    const compare = uri.localeCompare(data['uri'])
                    if (compare === 0) {
                        browser.storage.local.get("data").then(gotdata, onError);
                    }
                }
            )
        })

function clean_url_string(url){
    let temp_clean_uri = url.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"")
    url = temp_clean_uri.replace(/\s{2,}/g,"")
    return url
}

$("#analyze").click(function(event){
    uri = browser.tabs.query({currentWindow: true, active: true}).then(
        (tabs_info) => {
            return tabs_info[0].url;
        }
    )
    uri.then((result) => {
        let message = {
                name: result
            }

    $.post("http://127.0.0.1:5000/predict", JSON.stringify(message), function(response){

        let data = {
            uri: message['name'],
            news_pred: response.prediction.news,
            polarity_pred: response.prediction.polatiry,
            subjectivity_pred: response.prediction.subjectivity
        }

        browser.storage.local.set({data}).then(setItem, onError);
        browser.storage.local.get("data").then(gotdata, onError);
    });
    });
})
