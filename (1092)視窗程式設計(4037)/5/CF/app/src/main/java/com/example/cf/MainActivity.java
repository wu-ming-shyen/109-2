package com.example.cf;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.widget.EditText;
import android.widget.RadioGroup;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements RadioGroup.OnCheckedChangeListener, TextWatcher {

    RadioGroup unit;
    EditText value;
    TextView degC;
    TextView degF;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        unit = (RadioGroup)findViewById(R.id.unit);
        unit.setOnCheckedChangeListener(this);

        value = (EditText)findViewById(R.id.value);
        value.addTextChangedListener(this);

        degC = (TextView)findViewById(R.id.degC);
        degF = (TextView)findViewById(R.id.degF);
    }

    private void calc() {

        double val,c,f;
        String str = value.getText().toString();
        try{
            val = Double.parseDouble(str);
        }catch(Exception e){
            val = 0;
        }


        if(unit.getCheckedRadioButtonId()==R.id.unitF){
            f = val;
            c = (f-32)*5/9;
        }
        else {
            c = val;
            f = c*9/5+32;
        }

        degC.setText(String.format("%.1f",c)+getResources().getString(R.string.charC));
        degF.setText(String.format("%.1f",f)+getResources().getString(R.string.charF));
    }

    @Override
    public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

    }

    @Override
    public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

    }

    @Override
    public void afterTextChanged(Editable editable) {
        calc();
    }

    @Override
    public void onCheckedChanged(RadioGroup radioGroup, int i) {
        calc();
    }
}