package com.example.memo;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    EditText Name1,Name2,Phone;
    TextView Show;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Name1 = (EditText) findViewById(R.id.name1);
        Name2 = (EditText) findViewById(R.id.name2);
        Phone = (EditText) findViewById(R.id.phone);
        Show = (TextView) findViewById(R.id.textView);
    }
    public void onclick(View v){
        Show.setText(Name1.getText().toString()+" "+Name2.getText().toString()+"'s Phone is "+Phone.getText().toString());
    }
}