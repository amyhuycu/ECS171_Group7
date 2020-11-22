
function read_result(){
    const fs = require('fs');
    let rawdata = fs.readFileSync('result.json');
    let data = JSON.parse(rawdata);
    return data.result
}








