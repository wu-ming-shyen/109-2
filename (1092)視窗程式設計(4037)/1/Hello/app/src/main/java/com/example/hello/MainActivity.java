package com.example.hello;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }
    public void sayHello(View view){
        TextView textView = (TextView)findViewById(R.id.textView);
        EditText name = (EditText)findViewById(R.id.editText);

        textView.setText(name.getText().toString()+" Hello!");
    }
}