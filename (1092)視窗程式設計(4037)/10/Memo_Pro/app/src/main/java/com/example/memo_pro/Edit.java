package com.example.memo_pro;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class Edit extends AppCompatActivity {

    TextView txv;
    EditText edt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit);

        Intent it = getIntent();
        String str = it.getStringExtra("備忘");
        txv = (TextView)findViewById(R.id.textView);
        txv.setText(str.substring(0,2));
        edt = (EditText)findViewById(R.id.editText);
        if(str.length() > 3) edt.setText(str.substring(2));
    }

    public void onCancel(View view){
        setResult(RESULT_CANCELED);
        finish();
    }

    public void onSave(View view){
        Intent it2 = new Intent();
        it2.putExtra("備忘",txv.getText() + "" + edt.getText());
        setResult(RESULT_OK,it2);
        finish();
    }
}