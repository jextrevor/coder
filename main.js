(function(){
    instring = prompt("Enter the string to encode/decode");
    outstring = "";
    characters = [8203,8291];
    decode = false;
    characters.forEach(function(number){
        if(instring.indexOf(String.fromCharCode(number))!=-1){
            decode = true;
        }
    });
    inarray = instring.split('');
    if(decode){
        binarystring = "";
        inarray.forEach(function(character){
            if(character.charCodeAt(0) == characters[0]){
                binarystring += "0";
            }
            else if(character.charCodeAt(0) == characters[1]){
                binarystring += "1";
            }
        });
        binarychunks = binarystring.match(/.{1,16}/g);
        binarychunks.forEach(function(chunk){
            charcode = parseInt(chunk,2);
            outstring += String.fromCharCode(charcode);
        });
    }
    else{
        outstring = "[";
        binaryout = "";
        inarray.forEach(function(character){
            binarystring = character.charCodeAt(0).toString(2);
            while(binarystring.length < 16){
                binarystring = "0" + binarystring;
            }
            binaryout += binarystring;
        });
        binaryout = binaryout.split('');
        binaryout.forEach(function(character){
            if(character == "0"){
                outstring += String.fromCharCode(characters[0]);
            }
            if(character == "1"){
                outstring += String.fromCharCode(characters[1]);
            }
        });
        outstring += "]";
    }
    prompt("So you can copy...", outstring);
})();