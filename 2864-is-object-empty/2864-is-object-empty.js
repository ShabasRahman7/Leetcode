var isEmpty = function(obj) {
    let c=0;
    for(value in obj){
        c++;
    }
    if(c){
        return false
    }
    else{
        return true
    }
};