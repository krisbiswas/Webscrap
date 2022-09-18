package com.example.stateprogress;

import android.content.Context;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;

import androidx.annotation.Nullable;

public class StateBar extends LinearLayout {

    LinearLayout stateContainer;
    ImageView state1;
    ImageView state2;
    ImageView state3;

    public StateBar(Context context) {
        super(context);
    }

    public StateBar(Context context, @Nullable AttributeSet attrs) {
        super(context, attrs);
        LayoutInflater inflater = LayoutInflater.from(context);
        View root = inflater.inflate(R.layout.widget_state_progress, this);
        stateContainer = root.findViewById(R.id.linearLayout);
        state1 = root.findViewById(R.id.state1);
        state2 = root.findViewById(R.id.state2);
        state3 = root.findViewById(R.id.state3);
        state1.getDrawable().setState(new int[]{android.R.attr.state_enabled, -android.R.attr.state_active});
        state2.getDrawable().setState(new int[]{});
        state3.getDrawable().setState(new int[]{});
    }

    public StateBar(Context context, @Nullable AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    public StateBar(Context context, AttributeSet attrs, int defStyleAttr, int defStyleRes) {
        super(context, attrs, defStyleAttr, defStyleRes);
    }

//    @Override
//    public void ondrawIndicator()
//    {
//        if(mTextContainer != null)
//        {
//            mTextContainer.removeAllViews();
//            List<Float> complectedXPosition = mStepsViewIndicator.getCircleCenterPointPositionList();
//            if(mStepBeanList != null && complectedXPosition != null && complectedXPosition.size() > 0)
//            {
//                for(int i = 0; i < mStepBeanList.size(); i++)
//                {
//                    mTextView = new TextView(getContext());
//                    mTextView.setTextSize(TypedValue.COMPLEX_UNIT_SP, mTextSize);
//                    mTextView.setText(mStepBeanList.get(i).getName());
//                    int spec = View.MeasureSpec.makeMeasureSpec(0, View.MeasureSpec.UNSPECIFIED);
//                    mTextView.measure(spec, spec);
//                    // getMeasuredWidth
//                    int measuredWidth = mTextView.getMeasuredWidth();
//                    mTextView.setX(complectedXPosition.get(i) - measuredWidth / 2);
//                    mTextView.setLayoutParams(new ViewGroup.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT));
//
//                    if(i <= mComplectingPosition)
//                    {
//                        mTextView.setTypeface(null, Typeface.BOLD);
//                        mTextView.setTextColor(mComplectedTextColor);
//                    } else
//                    {
//                        mTextView.setTextColor(mUnComplectedTextColor);
//                    }
//
//                    mTextContainer.addView(mTextView);
//                }
//            }
//        }
//    }
}
