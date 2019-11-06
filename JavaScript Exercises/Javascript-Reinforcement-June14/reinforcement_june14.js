list = ["Totam", "ut", "odit", "quis", "Maiores", "unde", "EX", "EST", "corporis"]


for(let i = 0; i < list.length; i++) {
    if (list[i] == list[i].toLowerCase() & list[i].length > 4) {
        console.log('long and lowercase');
    }
    else if (list[i] == list[i].toLowerCase()) {
        console.log('lowercase');
    }
    else if (list[i].length > 4) {
        console.log('long');
    }
    else {
        console.log(`${list[i]}`);
    }
}