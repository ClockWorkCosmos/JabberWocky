import os; import random as r;
import termcolor; import time as t; import colorama;
from colorama import init; from termcolor import colored, cprint;
colorama.init();


counter=int(0); generated_keychr=int(0);
magic_number=int(0); filename=str("");
encryption_key=str(""); decrypted_content=str("");
encrypted_content=str(""); contents=str("");
pause_rate=float(1.5); miscellaneous_flag=False;


def clear_display():
    try:os.system("CLS");
    except:
        for x in range(0,20):print("");

def prRed(skk): 
    print("\033[91m {}\033[00m" .format(skk));
def prGreen(skk): 
    print("\033[92m {}\033[00m" .format(skk));
def prBlue(skk): 
    print("\033[96m {}\033[00m" .format(skk));

def prBanner():
    print(colored('..................    ..:::.    ..................','white','on_green'));
    print(colored('.................  ^JP#&&@&#GY!.  ................','white','on_green'));
    print(colored('................ :P@@@BP55PG&@@B!  ...............','white','on_green'));
    print(colored('............... ^#@@P^.     :J@@@?  ..............','white','on_green'));
    print(colored('..............  G@@P    ..    ?@@&: ..............','white','on_green'));
    print(colored('.............. ^@@@! ........ :&@@~ ..............','white','on_green'));
    print(colored('............   ^@@@^          :&@@!   ............','white','on_green'));
    print(colored('........... .~?5@@@5JJJJJJJJJJY@@@5?~. ...........','white','on_green'));
    print(colored('.......... ^B@@@@@@@@@@@@@@@@@@@@@@@@G^ ..........','white','on_green'));
    print(colored('.........  5@@@@@@@@@@@@@@@@@@@@@@@@@@Y ..........','white','on_green'));
    print(colored('.........  5@@@@@@@@@@#Y??Y#@@@@@@@@@@5  .........','white','on_green'));
    print(colored('.........  5@@@@@@@@@#:    :#@@@@@@@@@5 ..........','white','on_green'));
    print(colored('.........  5@@@@@@@@@&~    ~&@@@@@@@@@5 ..........','white','on_green'));
    print(colored('.........  5@@@@@@@@@@@?  ?@@@@@@@@@@@5 ..........','white','on_green'));
    print(colored('.........  5@@@@@@@@@@@~  !@@@@@@@@@@@5 ..........','white','on_green'));
    print(colored('.........  5@@@@@@@@@@#:::^&@@@@@@@@@@5 ..........','white','on_green'));
    print(colored('.........  P@@@@@@@@@@@&&&&@@@@@@@@@@@5 ..........','white','on_green'));
    print(colored('.......... ?@@@@@@@@@@@@@@@@@@@@@@@@@@7 ..........','white','on_green'));
    print(colored('..........  !PB####################B5~  ..........','white','on_green'));
    print(colored('...........   ......................   ...........','white','on_green'));
    print(""); print(colored('JabberWocky: Vigenere Cipher Utility','green','on_black'));
    print("--------------------------------------");
    print(colored('0. Compare Files','white','on_blue'));
    print(colored('1. Encrypt','white','on_magenta'));
    print(colored('2. Decrypt','white','on_magenta'));
    print(colored('3. Generate New Key','black','on_yellow'));
    print(colored('4. Create Custom Key','black','on_yellow'));
    print(colored('5. Load Key','black','on_yellow'));
    print(colored('6. Exit','white','on_red'));
    print("");

def compare_files(file_a,file_b):
    file_a_contents=str(); file_b_contents=str();
    character_matches=int(); comparison_len=int();
    similarity_score=float(0.00);
    with open(file_a,"r+",encoding="utf-8") as f:
        file_a_contents=str(f.read()); file_a_contents=[*file_a_contents];
        f.close();
    with open(file_b,"r+",encoding="utf-8") as f:
        file_b_contents=str(f.read()); file_b_contents=[*file_b_contents];
        f.close();
    if (len(file_b_contents)>=len(file_a_contents)):
        for x, _ in enumerate(file_a_contents):
            if (file_b_contents[x]==file_a_contents[x]):character_matches+=1;
            else:character_matches+=0;
    else:similarity_score=0.00;
    similarity_score=(character_matches*100)/len(file_a_contents);
    return similarity_score;
    

while True:
    clear_display(); prBanner();
    miscellaneous_flag=False;

    try: option=int(input(">> Select: "));
    except:
        print(colored('>> ERR: INVALID SELECTION (0-6)','white','on_red'));
        option=-1; option=int(-1); miscellaneous_flag=True;
        t.sleep(1.5);

    if (option==0):
        print("");
        print(colored('----------------------------------------------','blue','on_black'));
        filepath_a=input(">> COMPARE: "); filepath_b=input(">> TO: ");
        result=compare_files(filepath_b,filepath_a); print("");
        if (result>=95.00):prGreen("MATCH: "+str(result)+"%");
        else:prRed("MATCH: "+str(result));
        prRed("LOSS: "+str(100-result)+"%");
        print("");
        if ((100-result)>=1.00):print(colored('>> WARNING: FILE INTEGRITY LOSS EXCEEDS 1.0 %','black','on_yellow'));
        print(""); print(colored('----------------------------------------------','blue','on_black'));
        input(">> PRESS ENTER");

    elif (option==1):
        if (encryption_key==""):
            print(colored('>> ERR: NO KEY IMPORTED; PLEASE SELECT (5) FROM MENU.','white','on_red'));
            t.sleep(1.5);
        else:
            filename=str(input(">> Open: "));
            try:
                with open(filename,"r+", encoding="utf-8") as f:
                    contents=str(f.read()); contents=[*contents];
                    encryption_key=[*encryption_key]; counter=0;
                    for x, _ in enumerate(contents):
                        contents[x]=ord(contents[x]);
                        encryption_key[counter]=ord(encryption_key[counter]);
                        if (contents[x]<1):contents[x]=contents[x];
                        else:encrypted_content+=str(chr(contents[x]+encryption_key[counter]));
                        contents[x]=chr(contents[x]);
                        encryption_key[counter]=chr(encryption_key[counter]);
                        if (counter==int(len(encryption_key))-1):counter=0;
                        else:counter+=1;
                    contents=''.join(contents); encryption_key=''.join(encryption_key);
                    f.close();
                filename=str(input(">> Save as: "));
                with open(filename,"w+",encoding="utf-8") as f:
                    f.write(encrypted_content); encrypted_content="";
                    f.close();
                encryption_key="";
            except:print(colored('>> ERR: FILE NOT FOUND','white','on_red'));

    elif (option==2):
        if (encryption_key==""):
            print(colored('>> ERR: NO KEY IMPORTED; PLEASE SELECT (5) FROM MENU.','white','on_red'));
            t.sleep(1.5);
        else:
            filename=str(input(">> Open: "));
            try:
                with open(filename,"r+",encoding="utf-8") as f:
                    contents=str(f.read()); contents=[*contents];
                    encryption_key=[*encryption_key]; counter=0;
                    for x, _ in enumerate(contents):
                        contents[x]=ord(contents[x]);
                        encryption_key[counter]=ord(encryption_key[counter]);
                        if (contents[x]<1):contents[x]=contents[x];
                        else:
                            if (contents[x]-encryption_key[counter]<0):decrypted_content+=str(chr(contents[x]));
                            else:decrypted_content+=str(chr(contents[x]-encryption_key[counter]));
                        contents[x]=chr(contents[x]); encryption_key[counter]=chr(encryption_key[counter]);
                        if (counter==int(len(encryption_key))-1):counter=0;
                        else:counter+=1;
                    contents=''.join(contents); encryption_key=''.join(encryption_key);
                    f.close();
                filename=str(input(">> Save as: "));
                with open(filename,"w+",encoding="utf-8") as f:
                    f.write(decrypted_content);
                    decrypted_content=""; f.close();
                encryption_key="";
            except:print(colored('>> ERR: FILE NOT FOUND','white','on_red'));
    
    elif (option==3):
        encryption_key="";
        for x in range(0,25):
            generated_keychr=r.randint(89,128);
            encryption_key+=chr(generated_keychr);
        magic_number=r.randint(0,10); encryption_key+=str(magic_number);
        prGreen("Key: "+encryption_key); filename=str(input(">> Save as: "));
        encryption_key=[*encryption_key];
        for x, _ in enumerate(encryption_key):
            if (ord(encryption_key[x])>127):encryption_key[x]=ord(encryption_key[x]);
            else:encryption_key[x]=ord(encryption_key[x])+2;
            encryption_key[x]=chr(encryption_key[x]);
        encryption_key=str(''.join(encryption_key));
        with open(filename,"w",encoding="utf-8") as f:
            f.write(str(encryption_key)); f.close();

    elif (option==4):
        encryption_key=""; encryption_key=str(input(">> Custom key: "));
        filename=str(input(">> Save as: ")); encryption_key=[*encryption_key];
        for x, _ in enumerate(encryption_key):
            if (ord(encryption_key[x])>127):encryption_key[x]=ord(encryption_key[x]);
            else:encryption_key[x]=ord(encryption_key[x])+2;
            encryption_key[x]=chr(encryption_key[x]);
        encryption_key=str(''.join(encryption_key));
        with open(filename,"w", encoding="utf-8") as f:
            f.write(str(encryption_key)); f.close();

    elif (option==5):
        filename=str(input(">> Load key: "));
        try:
            with open(filename,"r",encoding="utf-8") as f:
                encryption_key=f.read(); f.close();
        except:
            print(colored('>> ERR: FILE NOT FOUND','white','on_red'));
            encryption_key=""; t.sleep(1.5);
        encryption_key=[*encryption_key];
        for x, _ in enumerate(encryption_key):
            if (ord(encryption_key[x])<1):encryption_key[x]=ord(encryption_key[x]);
            else:encryption_key[x]=ord(encryption_key[x])-2;
            encryption_key[x]=chr(encryption_key[x]);
        encryption_key=str(''.join(encryption_key));
        if (encryption_key!=""):prGreen(">> Using: "+encryption_key+" from "+filename);

    elif (option==6):break;
    else:
        if (miscellaneous_flag!=True):
            print(colored('>> ERR: INVALID SELECTION (1-6)','white','on_red'));
            t.sleep(1.5);   
    t.sleep(pause_rate); clear_display();
exit();
