function longestConsecutive(array, k) {
    if (array.length === 0 || k < 0 || k > array.length) {
        return ""
    }
    else {
        let word = '';
        let string = [];
        for (n = 0; n < array.length; n++) {
            if (k + n > array.length) {
                break
            }
            else {
                for (i = n; i < n+k; i++) {
                    word += array[i];
                }
                string.push(word);
                word = '';
            }
        }
        string.sort((a, b) => {
            return b.length - a.length ;
        })
        console.log(string[0]);
    }
}

longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3);
longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2);
