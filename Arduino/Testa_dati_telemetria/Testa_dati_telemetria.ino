typedef struct{
  uint8_t hour;
  uint8_t minute;
  uint8_t second;
  uint16_t microsecond;

  /*BIT A BIT DIVISION
   * bit 0-3 : number of satellites
   * bit 4-5 : Fix quality
   * bit 6 : East=1, West=0
   * bit 7 : North=1, South=0
   */
  uint8_t info;

  /*
   * HDOP REBUILD FORMULE: HDOP1->HDOP2
   */
  uint8_t HDOP1;
  uint8_t HDOP2;

  /*
   * LATITUDE REBUILD FORMULA: TO-DO
   */
  uint16_t Latitude1;
  uint32_t Latitude2;

  /*
   * LONGITUDE REBUILD FORMULA: TO-DO
   */
  uint32_t Longitude1;
  uint32_t Longitude2;

  /*
   * VEL REBUILD FORMULA: Vel1->Vel2
   */
  uint8_t Vel1;
  uint8_t Vel2;

  uint8_t decoded_data[24];
  uint8_t coded_data[35];

  // Must be between 0 and 63
  uint8_t headerIndex;
}block_4Hz;

typedef struct{
  uint8_t t_h2o;
  uint8_t t_air;
  uint8_t t_oil;

  uint8_t vbb;

  uint8_t lambda1_avg;
  uint8_t lambda1_raw;
  uint16_t klambda1;

  uint16_t injLow;
  uint16_t injHigh;

  uint8_t decoded_data[12];
  uint8_t coded_data[19];

  // Must be between 0 and 63
  uint8_t headerIndex;
}block_10Hz;

typedef struct{
  uint16_t rpm;
  uint16_t tps;

  uint16_t accelX;
  uint16_t accelY;
  uint16_t accelZ;

  uint16_t gyroX;
  uint16_t gyroY;
  uint16_t gyroZ;

  uint8_t potFSx;
  uint8_t potFDx;
  /*BIT A BIT DIVISION
   * bit 0-3 : overflow pot_Front_Sx
   * bit 4-7 : overflow pot_Front_Dx
   */
  uint8_t potFOver;
  uint8_t potFAccuracy;

  uint8_t potRSx;
  uint8_t potRDx;
  /*BIT A BIT DIVISION
   * bit 0-3 : overflow pot_Rear_Sx
   * bit 4-7 : overflow pot_Rear_Dx
   */
  uint8_t potROver;
  uint8_t potRAccuracy;

  uint8_t countFSx;
  uint8_t countFDx;
  /*BIT A BIT DIVISION
   * bit 0-3 : overflow count_Front_Sx
   * bit 4-7 : overflow count_Front_Dx
   */
  uint8_t countFOver;
  uint8_t dtF;
  uint8_t steering_encoder;

  uint8_t countRSx;
  uint8_t countRDx;
  /*BIT A BIT DIVISION
   * bit 0-3 : overflow count_Rear_Sx
   * bit 4-7 : overflow count_Rear_Dx
   */
  uint8_t countROver;
  uint8_t dtR;
  uint8_t gear;


  uint8_t decoded_data[36];
  uint8_t coded_data[51];

  // Must be between 0 and 63
  uint8_t headerIndex;
}block_100Hz;


void codeData4Hz(block_4Hz *block){
  block->coded_data[0] = 0x02;
  block->coded_data[1]=block->headerIndex;
  for (uint16_t i=0; i<sizeof(block->decoded_data)/3; i++){
    block->coded_data[4*i+2] = block->decoded_data[3*i]>>2 | 0x40;
    block->coded_data[4*i+3] = (block->decoded_data[3*i]&0x03)<<4 | block->decoded_data[3*i+1]>>4 | 0x40;
    block->coded_data[4*i+4] = (block->decoded_data[3*i+1]&0x0F)<<2 | block->decoded_data[3*i+2]>>6 | 0x40;
    block->coded_data[4*i+5] = (block->decoded_data[3*i+2] & 0x3F) | 0x40;
  }
  block->coded_data[34] = 0x03;
}

void setDecodedData4Hz(block_4Hz *block){
  block->headerIndex=0x04;
  block->decoded_data[0] = block->hour;
  block->decoded_data[1] = block->minute;
  block->decoded_data[2] = block->second;
  block->decoded_data[3] = block->microsecond>>8;
  block->decoded_data[4] = block->microsecond&0xFF;
  block->decoded_data[5] = block->info;
  block->decoded_data[6] = block->HDOP1;
  block->decoded_data[7] = block->HDOP2;
  block->decoded_data[8] = block->Latitude1>>8;
  block->decoded_data[9] = block->Latitude1&0xFF;
  block->decoded_data[10] = block->Latitude2>>24;
  block->decoded_data[11] = (block->Latitude2>>16)&0xFF;
  block->decoded_data[12] = (block->Latitude2>>8)&0xFF;
  block->decoded_data[13] = block->Latitude2&0xFF;
  block->decoded_data[14] = block->Longitude1>>24;
  block->decoded_data[15] = (block->Longitude1>>16)&0xFF;
  block->decoded_data[16] = (block->Longitude1>>8)&0xFF;
  block->decoded_data[17] = block->Longitude1&0xFF;
  block->decoded_data[18] = block->Longitude2>>24;
  block->decoded_data[19] = (block->Longitude2>>16)&0xFF;
  block->decoded_data[20] = (block->Longitude2>>8)&0xFF;
  block->decoded_data[21] = block->Longitude2&0xFF;
  block->decoded_data[22] = block->Vel1;
  block->decoded_data[23] = block->Vel2;
}

void codeData10Hz(block_10Hz *block){
  block->coded_data[0]=0x02;
  block->coded_data[1]=block->headerIndex;
  for (uint16_t i=0; i<sizeof(block->decoded_data)/3; i++){
    block->coded_data[4*i+2] = block->decoded_data[3*i]>>2 | 0x40;
    block->coded_data[4*i+3] = (block->decoded_data[3*i]&0x03)<<4 | block->decoded_data[3*i+1]>>4 | 0x40;
    block->coded_data[4*i+4] = (block->decoded_data[3*i+1]&0x0F)<<2 | block->decoded_data[3*i+2]>>6 | 0x40;
    block->coded_data[4*i+5] = (block->decoded_data[3*i+2] & 0x3F) | 0x40;
  }
  block->coded_data[18]=0x03;
}

void setDecodedData10Hz(block_10Hz *block){
  block->headerIndex=0x0A;
  block->decoded_data[0] = block->t_h2o;
  block->decoded_data[1] = block->t_air;
  block->decoded_data[2] = block->t_oil;
  block->decoded_data[3] = block->vbb;
  block->decoded_data[4] = block->lambda1_avg;
  block->decoded_data[5] = block->lambda1_raw;
  block->decoded_data[6] = block->klambda1>>8;
  block->decoded_data[7] = block->klambda1&0xFF;
  block->decoded_data[8] = block->injLow>>8;
  block->decoded_data[9] = block->injLow&0xFF;
  block->decoded_data[10] = block->injHigh>>8;
  block->decoded_data[11] = block->injHigh&0xFF;
}

void codeData100Hz(block_100Hz *block){
  block->coded_data[0]=0x02;
  block->coded_data[1]=block->headerIndex;
  for (uint16_t i=0; i<sizeof(block->decoded_data)/3; i++){
    block->coded_data[4*i+2] = block->decoded_data[3*i]>>2 | 0x40;
    block->coded_data[4*i+3] = (block->decoded_data[3*i]&0x03)<<4 | block->decoded_data[3*i+1]>>4 | 0x40;
    block->coded_data[4*i+4] = (block->decoded_data[3*i+1]&0x0F)<<2 | block->decoded_data[3*i+2]>>6 | 0x40;
    block->coded_data[4*i+5] = (block->decoded_data[3*i+2] & 0x3F) | 0x40;
  }
  block->coded_data[50]=0x03;
}

void setDecodedData100Hz(block_100Hz *block){
  block->headerIndex=0x3F;
  block->decoded_data[0] = block->rpm>>8;
  block->decoded_data[1] = block->rpm&0xFF;
  block->decoded_data[2] = block->tps>>8;
  block->decoded_data[3] = block->tps&0xFF;
  block->decoded_data[4] = block->accelX>>8;
  block->decoded_data[5] = block->accelX&0xFF;
  block->decoded_data[6] = block->accelY>>8;
  block->decoded_data[7] = block->accelY&0xFF;
  block->decoded_data[8] = block->accelZ>>8;
  block->decoded_data[9] = block->accelZ&0xFF;
  block->decoded_data[10] = block->gyroX>>8;
  block->decoded_data[11] = block->gyroX&0xFF;
  block->decoded_data[12] = block->gyroY>>8;
  block->decoded_data[13] = block->gyroY&0xFF;
  block->decoded_data[14] = block->gyroZ>>8;
  block->decoded_data[15] = block->gyroZ&0xFF;
  block->decoded_data[16] = block->potFSx;
  block->decoded_data[17] = block->potFDx;
  block->decoded_data[18] = block->potFOver;
  block->decoded_data[19] = block->potFAccuracy;
  block->decoded_data[20] = block->potRSx;
  block->decoded_data[21] = block->potRDx;
  block->decoded_data[22] = block->potROver;
  block->decoded_data[23] = block->potRAccuracy;
  block->decoded_data[24] = block->countFSx;
  block->decoded_data[25] = block->countFDx;
  block->decoded_data[26] = block->countFOver;
  block->decoded_data[27] = block->dtF;
  block->decoded_data[28] = block->steering_encoder;
  block->decoded_data[29] = block->countRSx;
  block->decoded_data[30] = block->countRDx;
  block->decoded_data[31] = block->countROver;
  block->decoded_data[32] = block->dtR;
  block->decoded_data[33] = block->gear;

  /*Aggiungere eventuali byte di controllo, avanzano*/
  block->decoded_data[34]=0;
  block->decoded_data[35]=0;
}

//Da personalizzare rispettando il numero corretto di elementi
//13
block_4Hz block4 = {1,1,1,1,1,1,1,1,1,1,1,1,1};
//9
block_10Hz block10 = {1,1,1,1,1,1,1,1,1};
//26
block_100Hz block100 = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};

unsigned long startTime;
unsigned long deltaTime;
int cycleCount = 0;
/*
byte packet4hz[] = {0x02, 0x04, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x03};
byte packet10hz[] = {0x02, 0x0A, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x03};
byte packet100hz[] = {0x02, 0x3F, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x40, 0x03};
*/

void setup() {
  
  // put your setup code here, to run once:
  Serial.begin(115200);
  startTime = millis();
  block4.headerIndex = 0x04;
  block10.headerIndex = 0x0A;
  block100.headerIndex = 0x3F;
  setDecodedData4Hz(&block4);
  setDecodedData10Hz(&block10);
  setDecodedData100Hz(&block100);
  codeData4Hz(&block4);
  codeData10Hz(&block10);
  codeData100Hz(&block100);
  
}

void loop() {
  
  // put your main code here, to run repeatedly:
  deltaTime = millis()-startTime;
  if( deltaTime >= 20 ) {
    Serial.print("ERRORE ERRORE ERRORE\n");
  }
  //Serial.print(deltaTime);
  if( cycleCount%250==0 ) {
    Serial.write(block4.coded_data, sizeof(block4.coded_data));
  }
  if( cycleCount%100==0 ) {
    Serial.write(block10.coded_data, sizeof(block10.coded_data));
  }
  if( cycleCount%10==0 ) {
    Serial.write(block100.coded_data, sizeof(block100.coded_data));
  }
  if( deltaTime >= 10 ) {
    cycleCount++;
    startTime = millis();
  }
  
}
