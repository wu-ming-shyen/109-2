package com.example.ticket;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void show(View v){
        TextView t = (TextView)findViewById(R.id.t);
        RadioGroup ticketType = (RadioGroup)findViewById(R.id.ticketType);
        switch (ticketType.getCheckedRadioButtonId()){
            case R.id.A:
                t.setText("台帛旅遊泡泡");
                break;
            case R.id.B:
                t.setText("國內旅遊方便又安全");
                break;
            case R.id.C:
                t.setText("去美國享受新冠肺炎病毒");
                break;
        }
    }
}