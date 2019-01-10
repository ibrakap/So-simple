#Bu yazılım ibrakap a aittir ve kendi şahsi çıkarları için yazılmıştır. Açık kaynaktır ve istenildiği gibi kullanılabilir.
import os
#Ekranı temizleyecek clear() fonksiyonu
def clear():
#for windows
 os.system('cls')
 #for linux or unix
 os.system('clear')
 #Bash tan çıkmak için kullanılacak olan fonksiyon
def çıkış():
 exit()
 #Hoşgeldin yazısı
print("""        **                                                   ***          ***** **                           *
    *****                                             *      ***      ******  ***                         **
    *  ***                                            ***      **     **   *  * **                         **
       ***                                             *       **    *    *  *  **                         **
      *  **         ******   ***  ****                         **        *  *   *                  ****    **
      *  **        ********   **** **** *    ****    ***       **       ** **  *        ****      * **** * **  ***
     *    **      *      **    **   ****    * ***  *  ***      **       ** ** *        * ***  *  **  ****  ** * ***
     *    **             *     **          *   ****    **      **       ** ***        *   ****  ****       ***   ***
    *      **           *      **         **    **     **      **       ** ** ***    **    **     ***      **     **
    *********          ***     **         **    **     **      **       ** **   ***  **    **       ***    **     **
   *        **          ***    **         **    **     **      **       *  **     ** **    **         ***  **     **
  *        **           ***   **         **    **     **      **          *      ** **    **    ****  **  **     **
  *****      **           **   ***        **    **     **      **      ****     ***  **    **   * **** *   **     **
 *   ****    ** *         **    ***        ***** **    *** *   *** *  *  ********     ***** **     ****    **     **
*     **      **          *                 ***   **    ***     ***  *     ****        ***   **             **    **
*                        *                                           *                                            *
 **                     *                                             **                                         *
                      *                                                                                        *
                                                                                                               *""")
while True:
    #Kullanıcıdan veri alır
    Bash = input(">>>")
    #Ekranı temizler
    if Bash == "Clear" or Bash == "clear" or Bash == "cls" or Bash == "temizle" or Bash == "Cls":
        clear()
    #Bash tan çıkar
    elif Bash == "Exit" or Bash == "exit" or Bash == "Çıkış" or Bash == "çıkış":
        çıkış()
    #Başlangıçtaki yazıya doyamayanlara :)
    elif Bash == "Bash" or Bash == "bash":
        print("        **                                                   ***          ***** **                           *")
        print("     *****                                             *      ***      ******  ***                         **")
        print("    *  ***                                            ***      **     **   *  * **                         **")
        print("       ***                                             *       **    *    *  *  **                         **")
        print("      *  **         ******   ***  ****                         **        *  *   *                  ****    **")
        print("      *  **        ********   **** **** *    ****    ***       **       ** **  *        ****      * **** * **  ***")
        print("     *    **      *      **    **   ****    * ***  *  ***      **       ** ** *        * ***  *  **  ****  ** * ***")
        print("     *    **             *     **          *   ****    **      **       ** ***        *   ****  ****       ***   ***")
        print("    *      **           *      **         **    **     **      **       ** ** ***    **    **     ***      **     **")
        print("    *********          ***     **         **    **     **      **       ** **   ***  **    **       ***    **     **")
        print("   *        **          ***    **         **    **     **      **       *  **     ** **    **         ***  **     **")
        print("  *        **           ***   **         **    **     **      **          *      ** **    **    ****  **  **     **")
        print("  *****      **           **   ***        **    **     **      **      ****     ***  **    **   * **** *   **     **")
        print(" *   ****    ** *         **    ***        ***** **    *** *   *** *  *  ********     ***** **     ****    **     **")
        print("*     **      **          *                 ***   **    ***     ***  *     ****        ***   **             **    **")
        print("*                        *                                           *                                            *")
        print(" **                     *                                             **                                         *")
        print("                       *                                                                                        *")
        print("                                                                                                               *")
    #Geçersiz komut hatasını önlemek için yazılmış satır
    elif Bash == "":
        Bash
    #Yardım satırı
    elif Bash == "Help" or Bash == "help" or Bash == "yardım":
        print("Clear,cls,temizle komutları bash i temizler\nExit,çıkış komutları bash ten çıkar\nBash komudu bash ilk açıldığındaki bash yazısını yazar")
    #int2hex conventer
    elif Bash == "int2hex" or Bash == "i2h":
        hex_int = int(input("Hex e çevirilecek sayı girin:"))
        print(hex_int,"sayısının hex hali =",hex(hex_int))
    #Süpriz bölümü
    elif Bash == "Suprize" or Bash == "suprize" or Bash == "süpriz":
        print("Basit hesap makinesi\nSayı Sayıcı\nHesap makinesi için hs yazın")
        Süpriz = input("Seçeneğiniz:")
        if Süpriz == "hs":
            Veri = input("Yapmak istediğiniz işlemi seçin\nToplama\nÇıkarma\nÇarpma\nBölme\n===")
    #Geçersiz girdiler için yanıt
    else:
        print("Geçersiz komut")
